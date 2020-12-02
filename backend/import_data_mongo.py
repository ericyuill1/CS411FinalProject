import boto3
import json
import rds_db as db
from flask import Flask, render_template, request, flash, redirect,url_for, jsonify, session, make_response
# dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
# table = dynamodb.Table("players")
results = db.get_set_game_count("MkLeo", "Marss")
print(len(results))
# p1 = "MkLeo" # data["player1"]
# p2 = "Marss" # data["player2"] 
# p1_data = table.get_item(Key={"tag" : p1})
# p2_data = table.get_item(Key={"tag" : p2})

# # print(p1_data['Item']["placings"])
# # print("\n\n")
# # print(p2_data['Item']["placings"])
# common_tournaments = {}
# var = json.loads(p1_data["Item"]["placings"])
# for i in var:
#     common_tournaments[i["key"]] = [i["placing"]]
# var2 = json.loads(p2_data["Item"]["placings"])
# for i in var2:
#     if i["key"] in common_tournaments:
#         common_tournaments[i["key"]].append(i["placing"])
# actual = {}
# for k in common_tournaments:
#     if len(common_tournaments[k]) == 2 and common_tournaments[k][0] > 0 and common_tournaments[k][1] > 0:
#         actual[k] = common_tournaments[k]
# # print(actual)
# cleaned_names = db.get_cleaned_names_by_keys(actual)
# actual2 = {}
# for k in actual:
#     actual2[cleaned_names[k]] = actual[k]
# print(actual2)
# with open("pgr_player_data.json", "r") as f:
#     data = json.load(f)
# # for d in data:
# #     print(d)
# #     print("\n")
# # with table.batch_writer() as batch:
# #     for d in data:
# #         batch.put_item(Item=d)
# resp = table.get_item(Key={"tag" : "zackray"})
# print(resp['Item'])

