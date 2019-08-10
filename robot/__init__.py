import os

from flask import Flask

try:
    from dotenv import load_dotenv
    APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
    dotenv_path = os.path.join(APP_ROOT, '.env')
    load_dotenv(dotenv_path)
except ImportError:
    pass

app = Flask(__name__)
app.config['GOOGLEMAPS_KEY'] = os.getenv('GOOGLEMAPS_KEY')

from . import robot

