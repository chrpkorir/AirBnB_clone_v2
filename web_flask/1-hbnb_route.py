#!/usr/bin/python3
"""Script that starts a Flask web application.
"""
from Flaks import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Function."""
    return "Hello HBNB!"


@qpp.route("/", strict_slashes=False)
def holberton():
    """Function."""
    return "HBNB"


if __name__ = "__main__":
    app.run(host='0.0.0.0', port=5000)
