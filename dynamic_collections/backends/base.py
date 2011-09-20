from django.conf import settings
from django.utils.importlib import import_module
from django.core.urlresolvers import get_mod_func

class CollectionsSearchBackendBase(object):
    "An abstract CollectionsSearchBackend that enforces proper implementation"
    
    def search(self, request, collection, backend_cleaned_request_representation):
        "Accepts a cleaned request representation (say a dictionary) and returns a generic set of objects"
        raise Exception('search is required to be implemented by CollectionsSearchBackend')
    
    def get_collection_items(self, request, collection):
        "Accepts a request and collection and returns a generic set of objects based on its db backend"
        if hasattr(settings, "COLLECTIONS_REQUEST_CLEANER"):
            request_cleaner = settings.COLLECTIONS_REQUEST_CLEANER
            if not callable(request_cleaner):
                mod_name, func_name = get_mod_func(request_cleaner)
                request_cleaner = getattr(import_module(mod_name), func_name)
            return self.search(request, collection, request_cleaner(request))
        else:
            raise Exception('COLLECTIONS_REQUEST_CLEANER setting not defined')