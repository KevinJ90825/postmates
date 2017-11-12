import urllib
from django.conf import settings
import json


class GeocodeHelper(object):

    def make_request(self, address):
        params = self.get_params(address)
        r = urllib.request.urlopen(self.API_URL + "?" + params)
        if r.getcode() != 200:
            return None
        return self.normalize_answer(json.loads(r.read()))

    def normalize_answer(self, ans):
        raise NotImplementedError

    def get_params(self, address):
        raise NotImplementedError

    @classmethod
    def query_address(cls, address, service="google"):
        geocoders = [GoogleGeocodeHelper(), HereGeocodeHelper()] if service == "google" else \
            [HereGeocodeHelper(), GoogleGeocodeHelper]

        for geo in geocoders:
            res = geo.make_request(address)
            if res:
                return res
        return {'status': 'failure', 'msg': 'Neither service gave a valid response'}

class GoogleGeocodeHelper(GeocodeHelper):

    API_URL = "https://maps.googleapis.com/maps/api/geocode/json"

    def get_params(self, address):
        return urllib.parse.urlencode({
            'address': address,
            'key': settings.GOOGLE_API_KEY
        })

    def normalize_answer(self, ans):
        result = ans['results'][0]
        return {
            'formatted_address': result['formatted_address'],
            'latitude': result['geometry']['location']['lat'],
            'longitude': result['geometry']['location']['lng'],
            'service': 'Google',
            'status': 'success'
        }


class HereGeocodeHelper(GeocodeHelper):
    API_URL = "https://geocoder.cit.api.here.com/6.2/geocode.json"

    def get_params(self, address):
        return urllib.parse.urlencode({
            'searchtext': address,
            'app_id': settings.HERE_APP_ID,
            'app_code': settings.HERE_APP_CODE
        })

    def normalize_answer(self, ans):
        result = ans['view'][0]['result'][0]
        return {
            'formatted_address': result['Location']['Address']['Label'],
            'latitude': result['Location']['DisplayPosition']['Latitude'],
            'longitude': result['Location']['DisplayPosition']['Longitude'],
            'service': 'Here',
            'status': 'success'
        }
