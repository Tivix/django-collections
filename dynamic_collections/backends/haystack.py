from dynamic_collections.backends.base import CollectionsSearchBackendBase

from haystack.query import SearchQuerySet

class CollectionsSearchBackend(CollectionsSearchBackendBase):
	"""A backend that uses Haystack to search for objects that belong to this collection."""
	
	def get_collection_items(self, terms):
		"Takes an array of strings and returns a set of objects"
		return []
