'''Set up a loop to iterate through the states list below  to change the state
name abbreviation in the URL, then fetch the data for each state, and populate
a text file with pretty results.
To make the code simple and elegant follow DRY principles
e.g., minimize local vars & avoid 3rd party libs which can be brittle'''

import urllib
import json

states = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]

for state in states:
    url = 'http://api.sba.gov/geodata/city_links_for_state_of/' + state + '.json'
    f = open(state, 'w')
    print >>f,  json.dumps(json.loads(urllib.urlopen(url).read()), indent=4, sort_keys=True)
    f.flush()
    f.close()
