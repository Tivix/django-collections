.. _pluggable:

==================
Pluggable Backends
==================

This app supports plugging in different backends to get the items in a collection.

You can use backends that come along with the app (see below) or define your own. All backends are required to implement two functions:

.. py:method:: get_collection_items(self, request, collection)

.. py:method:: search(self, backend_cleaned_request_representation)

The search function accepts a backend specific representation of the request and returns a set of generic objects.
It is called by get_collection_items function, which converts the request to the appropriate format by calling the configured function COLLECTIONS_REQUEST_CLEANER from the settings if it exists.


base.CollectionSearchBackend
-----------------------------
Includes a function get_collection_items that automatically calls COLLECTIONS_REQUEST_CLEANER and calls search() with its output.  It requires search be implemented by a child class.

Ideally backends should extend this class.

.. code-block:: python

	class CollectionsSearchBackendBase(object):
	    "An abstract CollectionsSearchBackend that enforces proper implementation"
	    
	    def search(self, backend_cleaned_request_representation):
	        "Accepts a cleaned request representation (say a dictionary) and returns a generic set of objects"
	        raise Exception('search is required to be implemented by CollectionsSearchBackend')
	    
	    def get_collection_items(self, request, collection):
	        "Accepts a request and collection and returns a generic set of objects based on its db backend"
	        if hasattr(settings, "COLLECTIONS_REQUEST_CLEANER"):
	            request_cleaner = settings.COLLECTIONS_REQUEST_CLEANER
	            self.search(request_cleaner(request, objects))
	        else:
	            raise Exception('COLLECTIONS_REQUEST_CLEANER setting not defined')

haystack.CollectionsSearchBackend
---------------------------------
The haystack CollectionsSearchBackend will use Haystack to get our collection items.
If you want to limit the models that are included in the filter you set a setting (COLLECTIONS_HAYSTACK_MODELS) to specify the models you wish to use.

.. code-block:: python

	COLLECTIONS_HAYSTACK_MODELS = ['app.Model', 'app.Model', 'app.Model']
	
It's search method works upon a dictionary (see below).  The get_collection_items function still only returns an array of generic objects.

.. code-block:: python
    
    {
       'app.Model1': {
           'var1': [val1, val2....],

       },
       .
       .
    }

Below is a sample model and index:

.. code-block:: python

	class Person(models.Model):
	    name = models.CharField(max_length=255, blank=True, null=True)
	    body = models.CharField(max_length=500, blank=True, null=True)
	    image = models.ImageField(upload_to="collection_item/", blank=True, null=True)
	    publish_date = models.DateTimeField(blank=True, null=True)
	    url = models.UrlField(max_length=255, blank=True, null=True)
	    
	class PersonIndex(SearchIndex):
	    title = CharField(document=True, use_template=True, model_attr='name')
	    description = CharField(model_attr='body')
	    image = ImageField(model_attr='image')
	    publish_time = DateTimeField(model_attr='publish_date')
	    url = UrlField(model_attr='url')
	    
	    def index_queryset(self):
	    	"Used when the entire index for model is updated"
	    	return Person.objects.all()
    
These indexes are the objects that are returned by the get_collection_items function.

