from flask import redirect, session, url_for
from app import app
from helpers import *

@app.route("/clear")
def clear():
    if "curridx" in session:
        session["curridx"] = 0
    if "fibs" in session:
        session["fibs"] = GetBaseCases()
    return redirect(url_for("current"))