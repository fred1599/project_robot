from nose.tools import assert_true

import requests


def test_request_response():
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

    assert_true(response.ok)
