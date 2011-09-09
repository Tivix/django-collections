.. _introduction:

==================================
Introduction to Django Collections
==================================

Django Collections provides a way to group and filter content through pre-set terms and configured aspects. 
It provides a user-friendly way of browsing content of different types, but with similar themes, and it doesn't require constant maintenance to add items to the collections.

Django Collections is a search interface. Each named Collection is really a pre-set search. It uses a search aggregator, like `Haystack`_\ , to provide the results and drive the filters (facets).

Potential uses
**************

Potential projects for which this application would be a good fit for:

* A blogging project where you'd like to to group different categories in varying ways to present blog posts to the user. Say you'd like to create a collection called "search engines" and would like to show to the user all blog posts that are tagged with "google", "yahoo", "bing" etc.

* A project where there are objects that have been tagged and you'd like to be able to group these tags in a arbitrary fashion and present the objects in a paginated list to the user.

.. _Haystack: http://haystacksearch.org/

Continue with :ref:`installation` 

