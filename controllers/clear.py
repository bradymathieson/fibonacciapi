from flask import session
from app import app
from helpers import *

@app.route("/clear")
def clear():
    if "curridx" not in session:
        pass
    session["curridx"] = 0
    return redirect(url_for("current"))