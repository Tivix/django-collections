from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from dynamic_collections.models import Collection
from dynamic_collections.forms import CollectionFilterForm

def collection_page(request, slug, template_name='collections/collection_page.html'):
    "Render the collection"

    collection = get_object_or_404(Collection, slug=slug)
    return render(request, template_name, {
        'collection': collection
    })

def collection_page_items(request, slug, template_name='collections/collection_page_items.html'):
    "Render the ajax collection page items"

    collection = get_object_or_404(Collection, slug=slug)
    
    form = CollectionFilterForm(request.REQUEST)
    paginator = Paginator(collection.items.all(), 10)
    page = paginator.page(1) 
    if form.is_valid():   
        paginator = Paginator(collection.items.all(), form.cleaned_data['per_page'])
        page = paginator.page(form.cleaned_data['page']) 
        
    return render(request, template_name, {
        'collection': collection,
        'form': form,
        'items': page.object_list,
        'page': page,
        'paginator': paginator,
        'type': type
    })
