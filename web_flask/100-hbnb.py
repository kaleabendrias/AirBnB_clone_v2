#!/usr/bin/python3
"""web application must be listening on 0.0.0.0"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb_filters():
    """sends states and amenities to 10-hbnb_filters.html"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)