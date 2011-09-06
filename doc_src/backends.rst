==================
Pluggable backends
==================

This app supports plugging in different backends to get the items in a collection.

You can use backends that come along with the app (see below) or define your own. All backends require to implement
certain functions:

.. py:method:: get_collection_items(terms)

The get_collection_items function accepts a list of terms (strings) and returns a set (or QuerySet) of objects.
The objects all extend this class:

.. code-block:: python

	class CollectionItem(models.Model):
	    title = models.CharField(max_length=255, blank=True, null=True)
	    description = models.CharField(max_length=500, blank=True, null=True)
	    image = models.ImageField(upload_to="collection_item/", blank=True, null=True)
	    publish_time = models.DateTimeField(blank=True, null=True)
	    url = models.UrlField(max_length=255, blank=True, null=True)

or at the very least requires the fields title, description, image, publish_time, and url.

haystack.CollectionsSearchBackend
---------------------------------
The haystack CollectionsSearchBackend will use Haystack to get our collection items.
In the configuration all you need to specify is the list of Haystack indexes you will use.
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
They are created like normal indexes for Haystack, but they still require the earlier mentioned fields.
As you can see from the example, the model doesn't need to match field names as long as in the index there is a field mapped over.
*********************************
