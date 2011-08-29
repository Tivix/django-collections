from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse
    
class Collection(models.Model):
    "Dynamic Collection"
    create_date = models.DateField()
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField( )
    text_body = models.TextField( )
    image = models.ImageField(upload_to="collection/", blank=True, null=True)

    seo_keywords = models.CharField(max_length=255)
    html_title = models.CharField(max_length=255)
    html_description = models.CharField(max_length=500)
    slug = models.SlugField()

    publish_time = models.DateTimeField(blank=True, null=True)
    expire_time = models.DateTimeField(blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse('collection_page', args=[self.slug])
        
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ["title"]
        
class CollectionItem(models.Model):
    "Dynamic Collection Item"
    collection = models.ForeignKey(Collection, related_name="items")
    
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    item = generic.GenericForeignKey('content_type', 'object_id')
    
    #represents the values of the item it wraps
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to="collection_item/", blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    
    def __unicode__(self):
        return str(self.collection) + ' ' + str(self.title)
