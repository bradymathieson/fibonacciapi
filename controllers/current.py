from flask import redirect, session, url_for
from app import app
from helpers import *

@app.route("/")
def index():
    return redirect(url_for("current"))

@app.route("/current")
def current():
    if "curridx" not in session:
        session["curridx"] = 0
    return str(GetFibValue(session["curridx"]))