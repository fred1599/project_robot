"""Flask init."""

from flask import Flask


app = Flask(__name__)

app.config["GOOGLEMAPS_KEY"] = "AIzaSyAENWDfGkNfvPEJP6t2ghSWh74tSnpszIM"

from . import robot
