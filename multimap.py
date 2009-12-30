import urllib
from utils import simplejson, partial2, RichResult

# http://www.multimap.com/openapidocs/1.2/web_service/ws_geocoding.htm

def geocode(q, api_key):
    base_url = 'http://developer.multimap.com/API/geocode/1.2/%s' % urllib.quote(api_key)
    json = simplejson.load(urllib.urlopen(base_url + '?' + urllib.urlencode({
            'qs': q,
            'output': 'json'
        })
    ))
    try:
        lon = json['result_set'][0]['point']['lon']
        lat = json['result_set'][0]['point']['lat']
    except (KeyError, IndexError):
        return RichResult((None, (None, None)), data=None)
    name = json['result_set'][0]['address']['display_name']
    return RichResult((name, (lat, lon)), data=json)

geocoder = partial2(geocode)
