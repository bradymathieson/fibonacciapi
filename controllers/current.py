from flask import session
from app import app
from helpers import *

@app.route("/current")
def current():
    if "curridx" not in session:
        session["curridx"] = 0
    return str(GetFibValue(session["curridx"]))