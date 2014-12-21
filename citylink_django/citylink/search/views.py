from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from citylink import settings

from django.utils import simplejson
from django.http import HttpResponse
from django.core import serializers
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

states = [
"AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
"HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
"MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
"NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
"SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]

def index(request, template_name="index.html"):
    return render_to_response(template_name, locals(), RequestContext(request)    )
    

import urllib, json
@login_required
def results(request, template_name="search/results.html"):
    """ template for displaying cities. """
    # get current query q
    q = request.GET.get('q', '').upper()
    state_found = True
    if q not in states:
        state_found = False
        return render_to_response(template_name, locals(), context_instance=RequestContext(request))

    cities = json.loads(urllib.urlopen('http://api.sba.gov/geodata/city_links_for_state_of/' + q + '.json').read())
    page_title = 'Cities for: ' + q
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))
