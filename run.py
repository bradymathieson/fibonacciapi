from app import app
from flask import session
from views import *

if __name__ == "__main__":
    app.run(debug=True)