from unittest.mock import Mock, patch

import requests
from nose.tools import assert_is_not_none, assert_list_equal

from project_robot.robot import app


@patch('requests.get')
def test_request_response(mock_get):

    mock_get.return_value = Mock(ok=True)

    search_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"

    params = {
        'input': 'paris',
        'inputtype': 'textquery',
        'fields': 'photos,formatted_address,name,rating,opening_hours,geometry',
        'key': app.config['GOOGLEMAPS_KEY'],
        'language': 'fr-FR',
    }

    mock_get.return_value.json.return_value = params

    response = requests.get(search_url, params=params)
    if not response.ok:
        response = None

    assert_is_not_none(response)


@patch('requests.get')
def test_request_response_1(mock_get):

    mock_get.return_value.ok = True

    search_url_wiki = "https://fr.wikipedia.org/w/api.php?"

    params_wiki = {
        'action': 'query',
        'prop': 'extracts',
        'exintro': '',
        'explaintext': '',
        'titles': 'paris',
        'format': 'json',
    }

    response = requests.get(url=search_url_wiki, params=params_wiki)
    if not response.ok:
        response = None

    assert_is_not_none(response)
