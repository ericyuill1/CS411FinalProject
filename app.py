# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 12:02:51 2020
@author: hp
"""

from flask import Flask, render_template, request, flash, redirect,url_for, jsonify, session 
from flask import Response,send_file

app = Flask(__name__)

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

@app.route('/insert',methods = ['post'])
def insert():
    actions = set(['insert', 'search','update','delete'])
    action = request.form['chooseField']
    # print(f"This is the action: {action}")
    results = None
    if action == "search":
        gamertag = request.form['baseInput']
        print(gamertag)
        results = db.get_player_by_gamertag(gamertag)
        print(len(results))
    elif action == "insert":
        gamertag = request.form['baseInput']
        results = db.insert_player_by_gamertag(gamertag)
    elif action == "update":
        old_gamer_tag = request.form['updateField1']
        new_gamer_tag = request.form['updateField2']
        results = db.update_player_by_gamertag(old_gamer_tag, new_gamer_tag)
    elif action == "delete":
        gamertag = request.form['baseInput']
        results = db.delete_player_by_gamertag(gamertag)
    elif action == "placement":
        placement = request.form['baseInput']
        results = db.get_players_by_placement(placement)
        for detail in results:
            var = detail
        return render_template('blank.html', var=var)
    if results == None:
        return redirect('index', code=307)
    elif len(results) == 0:
        var = "Sorry! That record was not found"
        return render_template('index.html', var=var)
    return render_template('index.html', var=results)



if __name__ == "__main__":
    
    app.run(debug=True)