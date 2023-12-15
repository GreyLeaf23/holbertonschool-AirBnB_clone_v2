#!/usr/bin/python3
"""Module starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)  # Holds the name of the module.


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Function returns a HTML page with a list
    of states when routed to
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(self):
    """Method for closing Flask connection"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Runs the application.
