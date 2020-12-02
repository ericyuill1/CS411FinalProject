# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 12:02:51 2020
@author: hp
"""

from flask import Flask, render_template, request, flash, redirect,url_for, jsonify, session, make_response
from flask import Response,send_file
import os
import json
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'
# https://medium.com/@eric.hung0404/deal-with-cors-without-flask-cors-an-example-of-react-and-flask-5832c44108a7
def build_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response
def build_actual_response(response):
    # response.headers.add("Access-Control-Allow-Origin", "*")
    return response
import rds_db as db
@app.route('/', methods=['get'])
@app.route('/index', methods=['get', 'post'])
def index():
    return render_template('index.html')


def handle_request(request):
    # print(request.form)
    actions = set(['insert', 'search','update','delete'])
    if request.method == 'POST':
        for action in actions:
            if request.form.get("gamertag_" + action) != None:
                return request.form.get("gamertag_" + action), action

# @app.route('/insert',methods = ['post'])
# def insert():
#     actions = set(['insert', 'search','update','delete'])
#     action = request.form['chooseField']
#     # print(f"This is the action: {action}")
#     results = None
#     if action == "search":
#         gamertag = request.form['baseInput']
#         results = db.get_player_by_gamertag(gamertag)
#     elif action == "insert":
#         gamertag = request.form['baseInput']
#         results = db.insert_player_by_gamertag(gamertag)
#     elif action == "update":
#         old_gamer_tag = request.form['updateField1']
#         new_gamer_tag = request.form['updateField2']
#         results = db.update_player_by_gamertag(old_gamer_tag, new_gamer_tag)
#     elif action == "delete":
#         gamertag = request.form['baseInput']
#         results = db.delete_player_by_gamertag(gamertag)
#     elif action == "placement":
#         placement = request.form['baseInput']
#         results = db.get_players_by_placement(placement)
#         for detail in results:
#             var = detail
#         return render_template('blank.html', var=var)
#     if results == None:
#         return redirect('index', code=307)
#     elif len(results) == 0:
#         var = "Sorry! That record was not found"
#         return render_template('index.html', var=var)
#     return render_template('index.html', var=results)
import requests


def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))



@app.route('/search', methods=['post'])
@cross_origin(supports_credentials=True)
def search():
    req = json.loads(request.data)
    gamertag = req['tag']
    # print(gamertag)
    results = db.get_player_by_gamertag(gamertag)
    # print(results[0][0])
    res = json.loads(results[0][0])
    # print(res)
    return build_actual_response(jsonify(res))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 3000), debug=True)