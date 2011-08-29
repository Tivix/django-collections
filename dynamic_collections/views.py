from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from models import Collection

def collection_page(request, slug, template_name='collections/collection_page.html'):
    "Render the collection"

    collection = get_object_or_404(Collection, slug=slug)
    return render(request, template_name, {
        'collection': collection
    })

def collection_page_items(request, slug, template_name='collections/collection_page_items.html'):
    "Render the ajax collection page items"

    collection = get_object_or_404(Collection, slug=slug)
    
    type = request.GET.get('type', 'list')
    per_page = request.GET.get('per_page', 10)
    page_number = request.GET.get('page', 1)
    
    paginator = Paginator(collection.items.all(), int(per_page))
    page = paginator.page(page_number)
    
    return render(request, template_name, {
        'collection': collection,
        'items': page.object_list,
        'page': page,
        'paginator': paginator,
        'type': type
    })
