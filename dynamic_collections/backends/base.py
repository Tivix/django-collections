from django.conf import settings

class CollectionsSearchBackendBase(object):
    "An abstract CollectionsSearchBackend that enforces proper implementation"
    
    def get_collection_items(self, request, collection):
        "Accepts a request and collection and returns a generic set of objects based on its db backend"
        raise Exception('get_collection_items is required to be implemented by CollectionsSearchBackend')

    def filter_further(self, request, objects):
        "Automatically calls the CALLBACK_FILTER_FUNCTION if it exists"
        if hasattr(settings, "CALLBACK_FILTER_FUNCTION"):
            filter = settings.CALLBACK_FILTER_FUNCTION
            return filter(request, objects)
        return objects 