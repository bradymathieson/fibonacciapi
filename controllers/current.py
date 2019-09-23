"""
/current route

Requires : an initialized session
Modifies : none
Effects  : returns a json of the current Fibonacci index and value
"""

from app import app
from helpers import GetJson
from flask import redirect, url_for

# Redirecting the root URI to the "current" endpoint
@app.route("/")
def index():
    return redirect(url_for("current"))

@app.route("/current")
def current():
    return GetJson()