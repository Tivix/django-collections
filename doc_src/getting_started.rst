.. _getting_started:

Getting Started
===============
If you have not installed Django Collections yet, go to the :ref:`installation` page.

Django settings
***************

You are required to specify a search backend. 
The search backend controls how the application gathers its collection items based on parameters. 

For example when using the Haystack backend

.. code-block:: python
    
    COLLECTIONS_SEARCH_BACKEND = 'dynamic_collections.backends.haystack.CollectionsSearchBackend'

Depending on your backend, you may need to set a number of other settings.


If you want filtering on your objects you will need to specify a callback function.

.. code-block:: python
    
    def filter_further(request, objects):
       return objects.filter(title__contains=request.GET['q'])
    COLLECTIONS_FILTER_CALLBACK = filter_further
    
:ref:`view` 



