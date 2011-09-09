.. _view:

==================
Custom view logic
==================

Collection Filter Callback
---------------------
Sometimes you need more than just a generic view.  You may find yourself needing to do some extra filtering on your generic objects.

In order to do this, you'll need to implement a filtering callback function.  
This function is called in the pluggable backends while querying your database.
It returns the query parameters needed to filter the backend.
There is a function in CollectionSearchBackend that automatically calls this function from the settings (COLLECTIONS_FILTER_CALLBACK) and has a matching signature.
While you are not required to extend this class for your backends, it does provide some convenience.

.. code-block:: python
    
    def filter_further_parameters(request, objects):
       return Q(title__contains=request.GET['q'])
    COLLECTIONS_FILTER_CALLBACK = filter_further_parameters
    
.. py:method:: filter_further_parameters(self, request, objects)

This method will pull the function from the settings (if it even exists) and call it with its own parameters.
This method needs to be called at some point within each CollectionsSearchBackend's get_collection_items method, or they need to implement the calling of the function themselves.
The exact implementation of filter_further will depend on the backend, as different backends provide different methods. 
This allows our users to take advantage of the different features backends add.

DynamicCollectionView
---------------------
Our app also uses a class based view called DynamicCollectionView.
The DynamicCollectionView __call__ function takes a slug, template_name, and extra_context.
The slug represents the slug of the collection, template_name allows you to override the template, and extra context allows you to pass extra context to the template.
Set these variables in the urls as you would any other view.

.. code-block:: python

	url(r'^(?P<slug>\w*)/$', DynamicCollectionView(), {
		'extra_context': ExtraForm()
	}, name='collection_page')

      
