import urllib
from utils import simplejson, partial2, RichResult

# http://code.google.com/apis/maps/documentation/geocoding/index.html

def geocode(q, api_key):
    json = simplejson.load(urllib.urlopen(
        'http://maps.google.com/maps/geo?' + urllib.urlencode({
            'q': q,
            'output': 'json',
            'oe': 'utf8',
            'sensor': 'false',
            'key': api_key
        })
    ))
    try:
        lon, lat = json['Placemark'][0]['Point']['coordinates'][:2]
    except (KeyError, IndexError):
        return RichResult((None, (None, None)), data=None)
    name = json['Placemark'][0]['address']
    return RichResult((name, (lat, lon)), data=json)

geocoder = partial2(geocode)
