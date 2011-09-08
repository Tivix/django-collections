.. _pluggable:

==================
Pluggable backends
==================

This app supports plugging in different backends to get the items in a collection.

You can use backends that come along with the app (see below) or define your own. All backends are required to implement one function:

.. py:method:: get_collection_items(request, collection)

The get_collection_items function accepts a request and a collection and returns a set of generic objects.
It needs to call the function COLLECTIONS_FILTER_CALLBACK from the settings if it exists and apply the function to its objects.

base.CollectionSearchBackend
-----------------------------
Includes a function filter_further that automatically calls COLLECTIONS_FILTER_CALLBACK.  It also requires get_collection_items be implemented by a child class.
Ideally backends should extend this class.

haystack.CollectionsSearchBackend
---------------------------------
The haystack CollectionsSearchBackend will use Haystack to get our collection items.
If you want to limit the models that are included in the filter you set a setting (COLLECTIONS_HAYSTACK_MODELS) to specify the models you wish to use.

.. code-block:: python

	COLLECTIONS_HAYSTACK_MODELS = ['app.Model', 'app.Model', 'app.Model']
	
It's filter_further method works upon a SearchQuerySet.  The get_collection_items function still only returns an array of generic objects.

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

