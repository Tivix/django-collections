.. _views:


Request Walkthrough
===================

1. A request is made by the user.
2. The request is routed to the view by urls, either DynamicCollectionView or some custom implementation.  This custom implementation is allowed to specify the template as well as any extra context the template may need.
3. __call__ is called on our DynamicCollectionView exactly like a view function would normally be called.
4. We load the collection based on the slug.
6. While within get_collection_items we need to call the function COLLECTION_FILTER_CALLBACK and get our parameters for the backend.
5. We load whichever backend the user has specified and call get_collection_items with our request and collection and loaded parameters.
7. Within get_collection_items we need to interact with the correlated db backend to get our objects.
8. The CollectionSearchBackend then returns the generic array of objects to the view.
9. The view uses the collection, collection items, template_name, and extra context to render the view.

