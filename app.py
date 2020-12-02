# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 12:02:51 2020
@author: hp
"""
import collections
from flask import Flask, render_template, request, flash, redirect,url_for, jsonify, session, make_response
from flask import Response,send_file
import os
import json
from flask_cors import CORS, cross_origin
import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table("players")
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


@app.route("/test", methods=["get", "post"])
@cross_origin(supports_credentials=True)
def get_pgr_players():
    results = db.export_pgr_players_to_json()
    obj_list = []
    for row in results:
        d = collections.OrderedDict()
        d['game'] = row[0]
        d['player_id'] = row[1]
        d['tag'] = row[2]
        d['all_tags'] = row[3]
        d['prefixes'] = row[4]
        d['social'] = row[5]
        d['country'] = row[6]
        d['state'] = row[7]
        d['region'] = row[8]
        d['placings'] = row[9]
        d['characters'] = row[10]
        d['alias'] = row[11]
        obj_list.append(d)
    j = json.dumps(obj_list)
    # with open('pgr_player_data.json', 'w') as f:
    #     f.write(j)
    return results

@app.route("/headtohead", methods=["post"])
@cross_origin(support_credentials=True)
def get_head_to_head():
    data = json.loads(request.data)
    p1 = data["player1"]
    p2 = data["player2"] 
    p1_data = table.get_item(Key={"tag" : p1})
    p2_data = table.get_item(Key={"tag" : p2})
    # print(p1_data["placings"])
    common_tournaments = {}
    var = json.loads(p1_data["Item"]["placings"])
    for i in var:
        common_tournaments[i["key"]] = [i["placing"]]
    var2 = json.loads(p2_data["Item"]["placings"])
    for i in var2:
        if i["key"] in common_tournaments:
            common_tournaments[i["key"]].append(i["placing"])
    actual = {}
    for k in common_tournaments:
        if len(common_tournaments[k]) == 2 and common_tournaments[k][0] > 0 and common_tournaments[k][1] > 0:
            actual[k] = common_tournaments[k]
    # print(actual)
    cleaned_names = db.get_cleaned_names_by_keys(actual)
    actual2 = {}
    
    for k in actual:
        actual2[cleaned_names[k]] = actual[k]
    obj_list = []
    for row in actual2:
        d = collections.OrderedDict()
        d['tournament'] = row
        d['placings'] = actual2[row]
        obj_list.append(d)
    # print(actual2)
    # print(jsonify(j))
    return jsonify(obj_list)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 3000), debug=True)