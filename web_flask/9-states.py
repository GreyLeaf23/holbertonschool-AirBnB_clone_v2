#!/usr/bin/python3
"""Module starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    state_dic = storage.all(State)
    state = None
    for obj in state_dic.values():
        if obj.id == id:
            state = obj
    return render_template('9-states.html', states=state_dic, id=id,
                           state=state)


@app.teardown_appcontext
def teardown_db(self):
    """Method for closing Flask connection"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
