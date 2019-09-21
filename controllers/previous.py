from flask import session
from app import app
from helpers import *

@app.route("/previous")
def previous():
    if "curridx" not in session:
        pass
    session["curridx"] -= 1
    return str(GetFibValue(session["curridx"]))