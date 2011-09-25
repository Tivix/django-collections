from django.db.models import get_model
from django.conf import settings

from dynamic_collections.backends.base import CollectionsSearchBackendBase

class CollectionsSearchBackend(CollectionsSearchBackendBase):
    """A backend that uses Haystack to search for objects that belong to this collection."""
    
    def search(self, request, collection, filter_parameters, order_parameters):
        if hasattr(settings, "COLLECTIONS_DJANGO_MODEL"):
            app_model = settings.COLLECTIONS_DJANGO_MODEL.split('.')
            django_model = get_model(*app_model)
            
            objects = django_model.objects.all()
            if not isinstance(filter_parameters, dict):       
                filter_parameters = {}
            
            if hasattr(settings, "COLLECTIONS_DJANGO_FIELD"):
                filter_parameters[settings.COLLECTIONS_DJANGO_FIELD + '__search'] = ' | '.join(collection.parameters.split(',')).strip(' |')  
            
            objects = objects.filter(**filter_parameters)
            return objects
        else:
            raise Exception('COLLECTIONS_DJANGO_MODEL setting not defined')
