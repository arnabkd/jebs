from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'bysykkel.views.index'),
	url(r'^(?P<rack_id>\d+)/$', 'bysykkel.views.detail'),
	url(r'^update/', 'bysykkel.views.update_static_racks'),
    # Examples:
    # url(r'^$', 'jebs.views.home', name='home'),
    # url(r'^jebs/', include('jebs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
    # Uncomment the next line to enable the admin:
   	url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': 'media'}),
)