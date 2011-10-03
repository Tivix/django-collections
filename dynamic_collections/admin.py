# -*- coding:  utf-8 -*-

from django.contrib import admin
from django.db import models
from models import *

class CollectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
    try:
        from tinymce.widgets import TinyMCE
        
        formfield_overrides = {
            models.TextField: {'widget': TinyMCE},
        }
    except ImportError: pass
    
admin.site.register(Collection, CollectionAdmin)
