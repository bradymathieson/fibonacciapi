"""
/clear route

Requires : none
Modifies : the current index and stored Fibonacci values
Effects  : clears out the user-triggered computation in Fibonacci values,
           and starts the user back at the beginning of the sequence
"""

from app import app
from flask import redirect, session, url_for

@app.route("/clear")
def clear():
    session["idx"] = 0
    session["fibs"] = [0, 1]
    return redirect(url_for("current"))