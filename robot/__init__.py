from flask import Flask


app = Flask(__name__)

is_production = os.environ.get('IS_HEROKU', None)
app.config['GOOGLEMAPS_KEY'] = 'AIzaSyAENWDfGkNfvPEJP6t2ghSWh74tSnpszIM'

from . import robot