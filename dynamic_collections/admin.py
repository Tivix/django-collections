# -*- coding:  utf-8 -*-

from django.contrib import admin
from models import *

class CollectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(Collection, CollectionAdmin)
