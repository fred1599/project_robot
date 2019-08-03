from nose.tools import assert_true
from robot import app

import requests


def test_request_response():
    search_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"

    params = {
        'input': 'paris',
        'inputtype': 'textquery',
        'fields': 'photos,formatted_address,name,rating,opening_hours,geometry',
        'key': app.config['GOOGLEMAPS_KEY'],
        'language': 'fr-FR',
    }

    response = requests.get(search_url, params=params)

    assert_true(response.ok)
