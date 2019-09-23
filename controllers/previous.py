"""
/previous route

Requires : an initialized session
Modifies : the current index, decreases by 1
Effects  : decreases the user by one index in the Fibonacci sequence, and returns a
           json with this previous value in the sequence. Checks to make sure the
           index does not become negative.
"""

from app import app
from helpers import GetJson
from flask import jsonify, session

@app.route("/previous")
def previous():
    if session["idx"] == 0:
        return jsonify({
            "error": "The index cannot go below zero."
        })
    session["idx"] -= 1
    return GetJson()