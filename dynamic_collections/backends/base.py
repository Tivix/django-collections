from django.conf import settings

class CollectionsSearchBackendBase(object):
    "An abstract CollectionsSearchBackend that enforces proper implementation"
    
    def search(self, backend_cleaned_request_representation):
        "Accepts a cleaned request representation (say a dictionary) and returns a generic set of objects"
        raise Exception('search is required to be implemented by CollectionsSearchBackend')
    
    def get_collection_items(self, request, collection):
        "Accepts a request and collection and returns a generic set of objects based on its db backend"
        if hasattr(settings, "COLLECTIONS_REQUEST_CLEANER"):
            request_cleaner = settings.COLLECTIONS_REQUEST_CLEANER
            return self.search(request_cleaner(request))
        else:
            raise Exception('COLLECTIONS_REQUEST_CLEANER setting not defined')