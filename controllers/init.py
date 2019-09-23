"""
before_request route

Requires : none
Modifies : the current index and stored Fibonacci values
Effects  : initializes the session variables if not already initialized. Checked
           before every request in our API, which is necessary, as all of them
           besides /clear require a session initialization.
"""

from app import app
from flask import session

@app.before_request
def init():
    if "idx" not in session:
        session["idx"] = 0
    if "fibs" not in session:
        session["fibs"] = [0, 1]