# -*- coding:  utf-8 -*-

from django.contrib import admin
from models import *
from tinymce.widgets import TinyMCE

class CollectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    widgets = {
        'text_body': TinyMCE(attrs={}),
    }
    
admin.site.register(Collection, CollectionAdmin)
