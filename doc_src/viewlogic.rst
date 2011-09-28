.. _view:

==================
View logic
==================

DynamicCollectionView
---------------------
Our app also uses a class based view called DynamicCollectionView.
The DynamicCollectionView __call__ function takes a slug, template_name, load_backend, and extra_context.
The slug represents the slug of the collection, template_name allows you to override the template, and extra context allows you to pass extra context to the template.
You can set whether or not to load the backend, which is useful when using DynamicCollectionView for ajax views.

Set these variables in the urls as you would any other view.

.. code-block:: python

	url(r'^(?P<slug>\w*)/$', DynamicCollectionView(), {
		'extra_context': {'filter_form': ExtraForm()},
		'template_name': 'collections/custom_template.html'
	}, name='collection_page')

