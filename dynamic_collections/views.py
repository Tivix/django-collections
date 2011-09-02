from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from dynamic_collections.models import Collection

class DynamicCollectionView(object):
    
    def __call__(self, request, slug, template_name='collections/collection_page.html'):
        "Render the collection"
    
        collection = get_object_or_404(Collection, slug=slug)
        
        objects = []
        #hooks
        objects = self.filter_further(request, objects)
        
        return render(request, template_name, {
            'collection': collection,
            'objects': objects
        })
        
    def filter_further(self, request, objects):
        "Override this method if objects needs to be filtered further"
        return objects
