from django.conf import settings
from django.core import exceptions
from django.utils.importlib import import_module

def get_collection_backend():
    if not hasattr(settings, 'COLLECTIONS_SEARCH_BACKEND'):
        raise Exception("settings requires 'COLLECTIONS_SEARCH_BACKEND' be set")
    
    try:
        cb_module, cb_classname = settings.COLLECTIONS_SEARCH_BACKEND.rsplit('.', 1)
    except ValueError:
        raise exceptions.ImproperlyConfigured('%s isn\'t a collection search backend module' % settings.COLLECTIONS_SEARCH_BACKEND)
    try:
        mod = import_module(cb_module)
    except ImportError, e:
        raise exceptions.ImproperlyConfigured('Error importing collection search backend %s: "%s"' % (cb_module, e))
    try:
        cb_class = getattr(mod, cb_classname)
    except AttributeError:
        raise exceptions.ImproperlyConfigured('Collection Search Backend module "%s" does not define a "%s" class' % (mw_module, mw_classname))
    return cb_class()