from django.conf.urls.defaults import *
from citylink import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import os
#from django.contrib.auth.views import logout
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^search/', include('search.urls')),
    #(r'^accounts/', include('django.contrib.auth.urls')),
    )
urlpatterns += patterns('django.contrib.auth.views',
    (r'^accounts/login/$', 'login', 
     {'template_name': 'login.html', 'SSL': settings.ENABLE_SSL }, 'login'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root' : os.path.join(settings.CURRENT_PATH, 'static') }),
)

handler404 = 'citylink.views.file_not_found_404'
#handler500 = 'citylink.views.server_error_500'
