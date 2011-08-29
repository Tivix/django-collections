from django.conf.urls.defaults import *

urlpatterns = patterns('',
   url(r'^(?P<slug>\w*)/$', 'dynamic_collections.views.collection_page', name='collection_page'),
   url(r'^(?P<slug>\w*)/items/$', 'dynamic_collections.views.collection_page_items', name='collection_page_items'),
)
