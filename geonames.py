from utils import simplejson, RichResult
import urllib

# http://www.geonames.org/export/geonames-search.html

def geocode(q):
    data = simplejson.load(urllib.urlopen(
        'http://ws.geonames.org/searchJSON?' + urllib.urlencode({
            'q': q,
            'maxRows': 1,
            'lang': 'en',
            'style': 'full'
        })
    ))
    if not data['geonames']:
        return RichResult((None, (None, None)), data=None)
    
    place = data['geonames'][0]
    name = place['name']
    if place['adminName1'] and place['name'] != place['adminName1']:
        name += ', ' + place['adminName1']
    return RichResult((name, (place['lat'], place['lng'])), data=data)

# No API key required, but let's fulfil the contract anyway
geocoder = lambda x: geocode
