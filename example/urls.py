from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from dynamic_collections.views import DynamicCollectionView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'natgeo.views.home', name='home'),
     url(r'^collections/', include('dynamic_collections.urls')),
     
   url(r'^ajax/(?P<slug>\w*)/$', DynamicCollectionView(), {
    'template_name': 'ajaxcollection/collection_page.html',
    'load_backend': False
   }),
   url(r'^ajax/(?P<slug>\w*)/items/$', DynamicCollectionView(), {
    'template_name': 'ajaxcollection/collection_items.html'
   }),

    (r'^tinymce/', include('tinymce.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
#We should NEVER let Django do the media hosting on a live site
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )