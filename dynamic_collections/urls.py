from django.conf.urls.defaults import *

urlpatterns = patterns('',
   url(r'^(?P<slug>\w*)/$', 'dynamic_collections.views.collection_page', name='collection_page'),
)
