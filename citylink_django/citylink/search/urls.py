from django.conf.urls.defaults import *

urlpatterns = patterns('citylink.search.views',
    (r'^results/$','results',{'template_name': 'search/results.html'}, 'search_results'),
    (r'^$','index', {'template_name': 'index.html'}, 'catalog_home'),
)
