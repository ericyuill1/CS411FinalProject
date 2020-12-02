# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:34:18 2020
@author: hp
"""
import json
from aws_credentials import conn

#Table Creation
#cursor=conn.cursor()
#create_table="""
#create table Details (name varchar(200),email varchar(200),comment varchar(200),gender varchar(20) )
#
#"""
#cursor.execute(create_table)


'''
insert_player(playerId)
get_player(playerId)
'''
PGR_Players = (
    "MkLeo", "Samsora", "Tweek", "Nairo", "Marss", "Maister", "zackray",
    "Glutonny", "Dabuz", "Light", "Kameme", "Tea", "Shuton", "ESAM",
    "T", "Raito", "Kuro", "ProtoBanham", "WaDi", "Lea", "Dark Wizzy",
    "Cosmos", "Abadango", "Kome", "Choco", "Nietono", "LeoN", "Gackt",
    "Salem", "Raffi-X", "Elegant", "Pandarian", "Etsuji", "Umeki", "Nicko",
    "Ned", "VoiD", "Lui$", "ScAtt", "HIKARU", "Goblin", "BestNess", "Mr.R",
    "RFang", "Kola", "Riddles", "Kirihara", "Big D", "Ron"
)

def get_player_by_gamertag(tag):
    query = f"SELECT placings FROM players where tag='{tag}'"
    cur=conn.cursor()
    cur.execute(query)
    details = cur.fetchall()
    # player_list = []
    # for i in details:
    #     t = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])
    #     player_list.append(t)
    # j = json.dumps(player_list, indent=2)
    # print(j)
    # with open("player_data.json", "w") as f:
    #     f.write(j)
    return details
def get_cleaned_names_by_keys(keys):
    cur = conn.cursor()
    cleaned_names = {}
    for key in keys:
        query = "SELECT cleaned_name FROM tournament_info WHERE tournament_info.key = '{0}' ".format(key)
        cur.execute(query)
        details = cur.fetchall()
        cleaned_names[key] = details[0][0]
    return cleaned_names


def export_pgr_players_to_json():
    query = f"SELECT DISTINCT * FROM players where tag IN {PGR_Players} AND game='ultimate' GROUP BY tag"
    cur = conn.cursor()
    cur.execute(query)
    details = cur.fetchall()
    return details

def insert_player_by_gamertag(tag):
    query = f"INSERT INTO Player (gamer_tag,scraped) VALUES ('{tag}', 'F')"
    cur=conn.cursor()
    cur.execute(query)
    conn.commit()
    return

def update_player_by_gamertag(old_tag, new_tag):
    query = f"UPDATE Player SET gamer_tag = '{new_tag}' WHERE gamer_tag = '{old_tag}'"
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    return 

def delete_player_by_gamertag(tag):
    query = f"DELETE FROM Player WHERE gamer_tag = '{tag}'"
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    return

def get_players_by_placement(placement):
    query = f"SELECT * FROM Player P NATURAL JOIN EventStanding E NATURAL JOIN TournamentEvent T WHERE placement={placement} AND P.player_id = E.player_id AND T.tournament_id = E.tournament_id GROUP BY placement"
    # query = f"SELECT gamer_tag FROM Player P JOIN EventStanding E JOIN TournamentEvent T WHERE placement={placement} AND P.player_id = E.player_id AND T.tournament_id = E.tournament_id GROUP BY placement"
    cur = conn.cursor()
    cur.execute(query)
    details = cur.fetchall()
    return details


