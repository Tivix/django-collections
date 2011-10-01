from django.db import models 
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse

class Collection(models.Model):
    "Dynamic Collection"
    
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    body_text = models.TextField()
    
    parameters = models.CharField(max_length=255, help_text="A csv field representing the parameters for the backend")
    
    create_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)
    
    #advanced options
    slug = models.SlugField()
    image = models.ImageField(upload_to="collection/", blank=True, null=True)
        
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ["title"]

