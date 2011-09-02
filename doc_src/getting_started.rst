
Getting Started
===============

Django settings
***************

There are various simple settings that a Django project would need when using this applications.

.. code-block:: python

    COLLECTION_SOURCES = {
        	'haystack': {
        		'search_indexes': ('NoteIndex', 'FooIndex', ),		
        	}
        }


Specify which backend you'd like to use. For example when using the Haystack backend:

.. code-block:: python

    COLLECTIONS_SEARCH_BACKEND = 'dynamic_collections.backends.haystack.CollectionsSearchBackend'
