from django.conf import settings
from django.utils.importlib import import_module
from django.core.urlresolvers import get_mod_func

class CollectionsSearchBackendBase(object):
    "An abstract CollectionsSearchBackend that enforces proper implementation"
    
    def _get_parameters_from_setting(self, var_name, request):
        "Get the parameters from the function specified in the settings"
        if hasattr(settings, var_name):
            request_cleaner = getattr(settings, var_name)
            if not callable(request_cleaner):
                mod_name, func_name = get_mod_func(request_cleaner)
                request_cleaner = getattr(import_module(mod_name), func_name)
                return request_cleaner(request)
        return None
        
    def search(self, request, collection, filter_parameters, order_parameters):
        "Accepts a cleaned request representation (say a dictionary) and returns a generic set of objects"
        raise Exception('search is required to be implemented by CollectionsSearchBackend')
    
    def get_collection_items(self, request, collection):
        "Accepts a request and collection and returns a generic set of objects based on its db backend"
        
        return self.search(request, collection, 
                           self._get_parameters_from_setting("COLLECTIONS_FILTER_CLEANER", request),
                           self._get_parameters_from_setting("COLLECTIONS_ORDER_CLEANER", request))