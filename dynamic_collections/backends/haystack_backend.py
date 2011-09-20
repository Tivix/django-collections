from django.db.models import get_model
from django.conf import settings
from django.utils.importlib import import_module
from django.core.urlresolvers import get_mod_func

from haystack.query import SearchQuerySet

from dynamic_collections.backends.base import CollectionsSearchBackendBase

class CollectionsSearchBackend(CollectionsSearchBackendBase):
	"""A backend that uses Haystack to search for objects that belong to this collection."""
	
	def search(self, request, collection, backend_cleaned_request_representation):
		
		parameters = ' | '.join(collection.parameters.split(','))
		
		objects = SearchQuerySet().filter(content=parameters)
		if hasattr(settings, "COLLECTIONS_HAYSTACK_MODELS"):
			haystack_models = settings.COLLECTIONS_HAYSTACK_MODELS
			
			#if we're a string pull out the function
			if isinstance(haystack_models, str):
				mod_name, func_name = get_mod_func(haystack_models)
				haystack_models = getattr(import_module(mod_name), func_name)

            #if we're a function pull out the models
			if callable(haystack_models):
				haystack_models = haystack_models(request)
            
			model_list = []
			if isinstance(backend_cleaned_request_representation, dict):
				objects = objects.filter(**backend_cleaned_request_representation)
			for haystack_model in haystack_models:
				app_model = haystack_model.split('.')
				model_list.append(get_model(*app_model))
			objects.models(*model_list)
		return objects
    
