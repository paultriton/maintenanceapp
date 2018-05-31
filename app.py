#app.py
"""imports"""
from flask import Flask, jsonify

APP = Flask(__name__)

REQUESTS = [{'id':1, 'request':'request1', 'status':'pending', 'username':'josh'},
            {'id':2, 'request':'request2', 'status':'approved', 'username':'Ethan'},
            {'id':3, 'request':'request3', 'status':'resolved', 'username':'Wilson'},
            {'id':4, 'request':'request4', 'status':'rejected', 'username':'Tom'}]

@APP.route('/api/v1/users/requests')
def index():
    """returns all"""
    return jsonify(REQUESTS)

if __name__ == '__main__':
    APP.run(debug=True)
