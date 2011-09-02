==================
Pluggable backends
==================

This app supports plugging in different backends to get the items in a collection.

You can use backends that come along with the app (see below) or define your own. All backends require to implement
certain functions:

.. py:class:: MyCustomBackend
    .. py:method:: get_collection_items(terms)

The get_collection_items function accepts a list of terms (strings) and returns a set (or QuerySet) of objects.


haystack.CollectionsSearchBackend
*********************************
