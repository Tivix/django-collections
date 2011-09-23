from django.db.models import get_model
from django.conf import settings

from dynamic_collections.backends.base import CollectionsSearchBackendBase

class CollectionsSearchBackend(CollectionsSearchBackendBase):
    """A backend that uses Haystack to search for objects that belong to this collection."""
    
    def search(self, request, collection, backend_cleaned_request_representation):
        if hasattr(settings, "COLLECTIONS_DJANGO_MODEL"):
            app_model = settings.COLLECTIONS_DJANGO_MODEL.split('.')
            django_model = get_model(*app_model)
            
            if isinstance(backend_cleaned_request_representation, dict):                      
                
                if hasattr(settings, "COLLECTIONS_DJANGO_FIELD"):
                    backend_cleaned_request_representation[settings.COLLECTIONS_DJANGO_FIELD + '__search'] = ' | '.join(collection.parameters.split(',')).strip(' |')
                    
                    objects = django_model.objects.filter(**backend_cleaned_request_representation)
                    return objects
                else:
                    raise Exception('COLLECTION_DJANGO_FIELD setting not defined')
            else:
                raise Exception('COLLECTIONS_REQUEST_CLEANER for models.CollectionSearchBackend must return a dict of kwargs for the Django model filter function')
        else:
            raise Exception('COLLECTIONS_DJANGO_MODEL setting not defined')
