""" app.py"""
from flask import Flask, jsonify

APP = Flask(__name__)

#user requests with thier details
REQUESTS = [{'id':1, 'request':'first request', 'status':'pending', 'user':'blake'},
            {'id':2, 'request':'second request', 'status':'accepted', 'user':'clement'},
            {'id':3, 'request':'third request', 'status':'resolved', 'user':'rob'},
            {'id':4, 'request':'fourth request', 'status':'rejected', 'user':'ethan'}]

@APP.route('/api/v1/users/requests/<request_id>', methods=['GET'])
def get_one_request(request_id):
    """ Returns single request """

    request_found = [request for request in REQUESTS if request['id'] == int(request_id)]

    if request_found:
        return jsonify({'request':request_found[0]})
    return "no request found"
