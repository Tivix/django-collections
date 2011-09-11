from dynamic_collections.backends.base import CollectionsSearchBackendBase

from haystack.query import SearchQuerySet

class CollectionsSearchBackend(CollectionsSearchBackendBase):
	"""A backend that uses Haystack to search for objects that belong to this collection."""
	
	def search(self, backend_cleaned_request_representation):
		objects = SearchQuerySet().all()
		return objects
    
