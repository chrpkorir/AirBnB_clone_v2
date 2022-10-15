#!/usr/bin/python3
"""A script that starts a Flask web app
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Function"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def holberton():
    """Function"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Function"""
    return "C %s" % text.replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
