from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from dynamic_collections.models import Collection

def collection_page(request, slug, template_name='collections/collection_page.html'):
    "Render the collection"

    collection = get_object_or_404(Collection, slug=slug)
    return render(request, template_name, {
        'collection': collection
    })
