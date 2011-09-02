from django.db import models 
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse
        
class Collection(models.Model):
    "Dynamic Collection"
    
    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    
    parameters = models.CharField(max_length=255)
    
    create_date = models.DateField()
    update_date = models.DateField()
    
    #advanced options
    slug = models.SlugField()
    image = models.ImageField(upload_to="collection/", blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse('collection_page', args=[self.slug])
        
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ["name"]
