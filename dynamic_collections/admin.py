# -*- coding:  utf-8 -*-

from django.contrib import admin
from models import *
    
class CollectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Content', {
            'fields': ('create_date', 'title', 'subtitle', 'description',
                       'text_body', 'image', 
#                       'credits', 
#                       'collection_tags_auto', 'collection_tags_manual'
                       )
        }),
        ('Metadata', {
#            'classes': ('collapse',),
            'fields': (
                       'html_title', 'html_description', 'seo_keywords',
                       'slug',
#                       'primary_category', 'secondary_categories',
#                       'audience_type',
#                       'featured_service', 'shared_services',
#                       'subjects', 'grades'
                       )
        }),
        ('Schedule', {
#            'classes': ('collapse',),
            'fields': ('publish_time', 'expire_time')
        }),
    )
    class Media:
        css = {
            "all": ("/static/c/jquery_custom_theme/jquery-ui-1.7.2.custom.css",)
        }
        js = ("/static/j/jquery.min.js", "/static/j/jquery-ui-1.7.2.custom.min.js",
              "/static/j/collections.admin.js",)

admin.site.register(CollectionItem)
admin.site.register(Collection, CollectionAdmin)
