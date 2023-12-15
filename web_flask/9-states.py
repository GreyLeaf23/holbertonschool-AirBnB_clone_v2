#!/usr/bin/python3
"""Module starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
    Function returns a HTML page with a
    list of states when routed to.
    """
    states = storage.all(State)
    return render_template('9-states.html', state=states)


@app.route('/states/<id>', strict_slashes=False)
def state(id):
    """
    Function returns a HTML page with a
    list of states when routed to.
    """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown_db(self):
    """Method for closing Flask connection"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
