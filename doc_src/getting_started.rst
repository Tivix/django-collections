.. _getting_started:

Getting Started
===============
If you have not installed Django Collections yet, go to the :ref:`installation` page.

Django settings
***************

COLLECTIONS_SEARCH_BACKEND
--------------------------
You are required to specify a search backend. 
The search backend controls how the application gathers its collection items based on parameters. 

For example when using the Haystack backend

.. code-block:: python
    
    COLLECTIONS_SEARCH_BACKEND = 'dynamic_collections.backends.haystack.CollectionsSearchBackend'


COLLECTIONS_REQUEST_CLEANER
---------------------------
Depending on your backend, you may need to set a number of other settings.

If you want custom filtering on your objects you will need to specify a cleaner function.
You can either set the variable COLLECTIONS_REQUEST_CLEANER to a function or specify its location via string.
Cleaners are required to return the filtering parameters in a way the backend understands.
This is generally done by returning a dictionary of kwargs for the backend's filtering function.

.. code-block:: python

	def request_cleaner(request):
	    return {'title__in': request.GET['q']}
	COLLECTIONS_REQUEST_CLEANER = request_cleaner

COLLECTIONS_HAYSTACK_MODELS
---------------------------
If using the haystack backend you can limit the models by specifying an array of strings that map to the models.
You can also specify a function that accepts a request and returns an array of strings that map to the models.
You can also specify this function with a string

.. code-block:: python

	COLLECTIONS_HAYSTACK_MODELS = ['app.Model1', 'app.Model2', 'app.Model3']
	
or

.. code-block:: python
	
	def haystack_models(request):
		return ['app.Model', 'app.Model', 'app.Model']
	COLLECTIONS_HAYSTACK_MODELS = haystack_models   
:ref:`view` 

