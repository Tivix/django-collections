from dynamic_collections.backends.base import CollectionsSearchBackendBase

from haystack.query import SearchQuerySet

class CollectionsSearchBackend(CollectionsSearchBackendBase):
	"""A backend that uses Haystack to search for objects that belong to this collection."""
	
	def search(self, backend_cleaned_request_representation):
		objects = SearchQuerySet().all()
		if hasattr(settings, "COLLECTIONS_HAYSTACK_MODELS"):
			model_list = []
			for haystack_model in settings.COLLECTIONS_HAYSTACK_MODELS:
				app_model = haystack_model.split('.')
				model_list.append(get_model(*app_model))
			objects.models(*model_list)
		return objects
    
