from django.conf.urls.defaults import *

from dynamic_collections.views import DynamicCollectionView

urlpatterns = patterns('',
   url(r'^(?P<slug>\w*)/$', DynamicCollectionView(), name='collection_page'),
)
