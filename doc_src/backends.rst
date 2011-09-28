.. _pluggable:

==================
Pluggable Backends
==================

This app supports plugging in different backends to get the items in a collection.

You can use backends that come along with the app (see below) or define your own. All backends are required to implement two functions:

.. py:method:: get_collection_items(self, request, collection)

The get_collection_items function accepts the request received by the view as well as the collection with the slug received by the view.
It returns a generic set of objects.

.. py:method:: search(self, request, collection, filter_parameters, order_parameters)

The search function accepts the request, collection, filtering parameters and ordering parameters and returns a set of generic objects.
It is called by get_collection_items function, which converts gets the filtering and ordering parameters from the request and the cleaner functions, if set.

.. code-block:: python

	def filter_cleaner(request):
	    return {'title__in': request.GET['q']}
	COLLECTIONS_FILTER_CLEANER = filter_cleaner
	
	
	def order_cleaner(request):
	    return [request.GET['order']]
	COLLECTIONS_ORDER_CLEANER = order_cleaner

base.CollectionSearchBackend
-----------------------------
Includes a function get_collection_items that automatically calls COLLECTIONS_FILTER_CLEANER and COLLECTIONS_ORDER_CLEANER and calls search() with its output.  It requires search be implemented by a child class.

Ideally backends should extend this class.

.. code-block:: python

	class CollectionsSearchBackendBase(object):
	    "An abstract CollectionsSearchBackend that enforces proper implementation"
	    
	    
	    def search(self, request, collection, filter_parameters, order_parameters):
	        "Accepts a cleaned request representation (say a dictionary) and returns a generic set of objects"
	        raise Exception('search is required to be implemented by CollectionsSearchBackend')
	    
	    def get_collection_items(self, request, collection):
	        "Accepts a request and collection and returns a generic set of objects based on its db backend"
	        
	        filter_cleaner = request.COLLECTIONS_FILTER_CLEANER
	        order_cleaner = request.COLLECTIONS_ORDER_CLEANER
	        return self.search(request, collection, filter_cleaner(request), order_cleaner(request))

haystack.CollectionsSearchBackend
---------------------------------
The haystack CollectionsSearchBackend will use Haystack (v1.2.5) to get our collection items.
If you want to limit the models that are included in the filter you set a setting (COLLECTIONS_HAYSTACK_MODELS) to specify the models you wish to use.

.. code-block:: python

	COLLECTIONS_HAYSTACK_MODELS = ['app.Model', 'app.Model', 'app.Model']
	
COLLECTIONS_HAYSTACK_MODELS can also be a callback function that accepts a request and returns the array of model strings.
This callback function can be specified in a string.

.. code-block:: python
	
	def haystack_models(request):
		return ['app.Model', 'app.Model', 'app.Model']
	COLLECTIONS_HAYSTACK_MODELS = haystack_models
	
The COLLECTIONS_FILTER_CLEANER function returns a dictionary of kwargs for the SearchQuerySet filter method.
The COLLECTIONS_ORDER_CLEANER function returns an array of args for the SearchQuerySet order_by method.  
The get_collection_items function still only returns an array of search indexes.

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

models.CollectionSearchBackend
---------------------------------
The models CollectionsSearchBackend will use Django models to get our collection items.
You specify the custom model to use with the COLLECTIONS_DJANGO_MODEL setting.

.. code-block:: python

	COLLECTIONS_DJANGO_MODEL = 'app.Model'
	
It's search method gives you access to the queryset methods available for your Django model.
The model you specify is what is returned by the get_collection_items function.
