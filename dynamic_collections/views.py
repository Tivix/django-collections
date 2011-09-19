from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from dynamic_collections.models import Collection
from dynamic_collections.utils import get_collection_backend

class DynamicCollectionView(object):
    
    def __call__(self, request, slug, template_name='collections/collection_page.html', extra_context={}):
        "Render the collection"
    
        collection = get_object_or_404(Collection, slug=slug)
        
        #get from backend
        backend = get_collection_backend()
        objects = backend.get_collection_items(request, collection)
        
        extra_context.update({
            'collection': collection,
            'objects': objects
        })
        return render_to_response(template_name, extra_context,
                                  context_instance=RequestContext(request))
