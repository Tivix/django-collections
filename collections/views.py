from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.template import RequestContext
from django.utils.translation import ugettext, ugettext_lazy as _

from models import Collection

def collection_page(request, slug):
    "Render the product category"

    collection = get_object_or_404(Collection, slug=slug)
    return render(request, 'collections/collection_page.html', {
        'collection': collection
    })

def collection_page_items(request, slug):
    "Render the ajax collection page items"

    collection = get_object_or_404(Collection, slug=slug)
    return render(request, 'collections/collection_page_items.html', {
        'collection': collection
    })
