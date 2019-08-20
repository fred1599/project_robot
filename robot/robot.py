import requests
from flask import render_template, request, redirect, Response
import re

from . import app
from .utils import parse


@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect('question')


@app.route('/question', methods=['GET', 'POST'])
def question():
    search_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
    search_url_wiki = "https://fr.wikipedia.org/w/api.php?"
    location, city, exact_address, parse_wiki, title = None, None, None, None, ''
    if request.method == 'GET':
        return render_template('robot_template.html', location=location,
                               city=city, wiki=parse_wiki, exact_address=exact_address)
    elif request.method == 'POST':
        q = request.form['question']
        if q:
            query = b' '.join(parse(q)).decode()
            params = {
                'input': query,
                'inputtype': 'textquery',
                'fields': 'photos,formatted_address,name,rating,opening_hours,geometry',
                'key': app.config['GOOGLEMAPS_KEY'],
                'language': 'fr-FR',
            }

            req = requests.get(url=search_url, params=params)
            result = req.json()

            ad = result['candidates'][0]['formatted_address'].split(',')
            if len(ad) == 3:
                street_name, city, country = map(str.strip, ad)
                title = street_name + ' ' + city
            elif len(ad) == 2:
                city, country = map(str.strip, ad)
                infos = city.split()
                if len(infos) == 2:
                    title = city + ' ' + country
                else:
                    title = infos[0]
            elif len(ad) == 1:
                country = ad[0].strip()
                title = country

            if ad:
                try:
                    infos_dict = result['candidates'][0]
                    location = infos_dict['geometry']['location']
                except IndexError:
                    exact_address = ''
                    location = {}

                params_wiki = {
                    'action': 'query',
                    'prop': 'extracts',
                    'exintro': '',
                    'explaintext': '',
                    'titles': ' '.join(re.findall('[a-zA-Z]+', b' '.join(parse(title)).decode())),
                    'format': 'json',
                }

                req_wiki = requests.get(url=search_url_wiki, params=params_wiki)
                result_wiki = req_wiki.json()

                #  Si adresse non trouvée par wikipedia
                #  On se renseigne sur la ville
                p = ''
                if 'query' in result_wiki:
                    pages = result_wiki['query']['pages']
                    if '-1' in pages:
                        infos = city.split()
                        if len(infos) == 2:
                            title = infos[1]
                        else:
                            title = city
                        params_wiki['titles'] = title
                        req_wiki = requests.get(url=search_url_wiki, params=params_wiki)
                        result_wiki = req_wiki.json()
                        for key in result_wiki['query']['pages']:
                            if 'extract' in result_wiki['query']['pages'][key]:
                                p += result_wiki['query']['pages'][key]['extract']
                    else:
                        for key in result_wiki['query']['pages']:
                            p += result_wiki['query']['pages'][key]['extract']

                    return render_template(
                        'robot_template.html', location=location,
                        city=city, wiki=p, exact_address=ad,
                    )
                else:
                    return redirect('question')
    else:
        return Response(status=400)
