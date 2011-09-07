from django.db import models 
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse

from haystack import site

from dynamic_collections.indexes import CollectionItemIndex

class CollectionItem(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to="collection_item/", blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    url = models.UrlField(max_length=255, blank=True, null=True)
    
site.register(CollectionItem, CollectionItemIndex)

