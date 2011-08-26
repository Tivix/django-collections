from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

    
class Collection(models.Model):
    "Dynamic Collection"
    create_date = models.DateField()
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField( )
    text_body = models.TextField( )
    image = models.ImageField(upload_to="collection/", blank=True, null=True)
#    credits = models.ForeignKey(Credit, blank=True, null=True)
#    collection_tags_auto = models.ForeignKey(KeyConcept, related_name="auto_collections")
#    collection_tags_manual = models.ManyToManyField(KeyConcept, related_name="manual_collections")
    
#    subjects = models.ManyToManyField(Subject)
#    grades = models.ManyToManyField(Grade)
#    shared_services = models.ManyToManyField(Service, related_name="collections")
#    featured_service = models.ForeignKey(Service, blank=True, null=True, related_name="featured_collection")
#
#    primary_category = models.ForeignKey(Category, related_name="featured_collection")
#    secondary_categories = models.ManyToManyField(Category, related_name="collections")
#
#    audience_type = models.ForeignKey(AudienceType)
#    
    seo_keywords = models.CharField(max_length=255)
    html_title = models.CharField(max_length=255)
    html_description = models.CharField(max_length=500)
    slug = models.SlugField()

    publish_time = models.DateTimeField(blank=True, null=True)
    expire_time = models.DateTimeField(blank=True, null=True)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ["title"]
        
class CollectionItem(models.Model):
    "Dynamic Collection Item"
    collection = models.ForeignKey(Collection)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    item = generic.GenericForeignKey('content_type', 'object_id')
    
    def __unicode__(self):
        return str(self.collection) + ' ' + str(self.item)

#class KeyConcept(models.Model):
#    "Key concept"
#    name = models.CharField(max_length=255)
#    def __unicode__(self):
#        return self.name
#    
#class Credit(models.Model):
#    "Credit filler"
#    name = models.CharField(max_length=255)
#    def __unicode__(self):
#        return self.name
#    
#class Category(models.Model):
#    "Category filler"
#    name = models.CharField(max_length=255)
#    def __unicode__(self):
#        return self.name
#    
#class AudienceType(models.Model):
#    "Audience Type filler"
#    name = models.CharField(max_length=255)
#    def __unicode__(self):
#        return self.name
#    
#class Service(models.Model):
#    "Service filler"
#    name = models.CharField(max_length=255)
#    def __unicode__(self):
#        return self.name
#    
#class Subject(models.Model):
#    "Subject filler"
#    name = models.CharField(max_length=255)
#    def __unicode__(self):
#        return self.name
#    
#class Grade(models.Model):
#    "Grade filler"
#    name = models.CharField(max_length=255)
#    def __unicode__(self):
#        return self.name
