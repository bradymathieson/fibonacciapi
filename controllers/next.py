"""
/next route

Requires : an initialized session
Modifies : the current index, increases by 1
Effects  : increases the user by one index in the Fibonacci sequence, and returns a
           json with the next value in the sequence. 
"""

from app import app
from helpers import GetJson
from flask import session

@app.route("/next")
def next():
    session["idx"] += 1
    return GetJson()