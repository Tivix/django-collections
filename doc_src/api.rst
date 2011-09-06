.. _api:

API Reference
=============

.. contents::
   :depth: 3
   
Models
********
   
Collection
------

Fields

* **title** - The title
    * CharField
    * Length: 255
* **subtitle** - The subtitle
    * CharField
    * Length: 255
* **description** - The description
    * TextField

* **parameters** - A csv-field of the terms that bind the Collection
    * CharField
    * Length: 255
    
* **create_timestamp** - Timestamp of when the Collection was created
    * DateTimeField
    * auto_now_add
* **update_timestamp** - Timestamp of the last time the Collection was modified
    * DateTimeField
    * auto_now
    
* **slug** - Slugified title
    * SlugField
    * Length: 150
* **image** - Optional image taken from one of its items
    * ImageField
    * blank=True, null=True
       
Backends
********

backends.haystack.CollectionsSearchBackend
------

get_collection_items
~~~~~~
Returns a haystack SearchQuerySet
    
Views
********

DynamicCollectionView
------

__call__
~~~~~~
Represents the view function

filter_further
~~~~~~
Hook-in function for filtering the collection items further