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
You can either set the variable to a function or specify a its location via string.

.. code-block:: python
    
    def request_haystack_backend_cleaner(request):
        d = {}
        form = MyForm(request.GET)
        if form.is_valid():
            d.update('app.Models1': form.cleaned_data['subjects'])
            d.update('app.Models2': form.cleaned_data['categories'])
        return d
    
    COLLECTIONS_REQUEST_CLEANER = request_haystack_backend_cleaner


COLLECTIONS_HAYSTACK_MODELS
---------------------------
If using the haystack backend you can limit the models by specifying an array of strings that map to the models.

.. code-block:: python

	COLLECTIONS_HAYSTACK_MODELS = ['app.Model1', 'app.Model2', 'app.Model3']
    
:ref:`view` 

