# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:34:18 2020
@author: hp
"""
import pymysql, json
conn = pymysql.connect(
    host = "panda-local.cmcngdzhrbgb.us-east-2.rds.amazonaws.com",
    port = 3306,
    user = "admin",
    password = "advaitejaeric",
    database = "teja"
)

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


# def get_player_by_gamertag(tag):
#     query = f"SELECT * FROM Player WHERE gamer_tag = '{tag}'"
#     cur=conn.cursor()
#     cur.execute(query)
#     details = cur.fetchall()
#     return details

# def insert_player_by_gamertag(tag):
#     query = f"INSERT INTO Player (gamer_tag,scraped) VALUES ('{tag}', 'F')"
#     cur=conn.cursor()
#     cur.execute(query)
#     conn.commit()
#     return

# def update_player_by_gamertag(old_tag, new_tag):
#     query = f"UPDATE Player SET gamer_tag = '{new_tag}' WHERE gamer_tag = '{old_tag}'"
#     cur = conn.cursor()
#     cur.execute(query)
#     conn.commit()
#     return 

# def delete_player_by_gamertag(tag):
#     query = f"DELETE FROM Player WHERE gamer_tag = '{tag}' AND scraped = 'F'"
#     cur = conn.cursor()
#     cur.execute(query)
#     conn.commit()
#     return

# def get_players_by_placement(placement):
#     query = f"SELECT * FROM Player P NATURAL JOIN EventStanding E NATURAL JOIN TournamentEvent T WHERE placement={placement} AND P.player_id = E.player_id AND T.tournament_id = E.tournament_id GROUP BY placement"
#     # query = f"SELECT gamer_tag FROM Player P JOIN EventStanding E JOIN TournamentEvent T WHERE placement={placement} AND P.player_id = E.player_id AND T.tournament_id = E.tournament_id GROUP BY placement"
#     cur = conn.cursor()
#     cur.execute(query)
#     details = cur.fetchall()
#     return details

def get_pgr50():
    query = f"select by_id from ranking_seasons where season = 2 and ranking_name = 'PGRU'"
    cur = conn.cursor()
    cur.execute(query)
    details = cur.fetchall()
    return json.loads(details[0][0])

def get_sets_by_list_of_player_ids(player_list):
    player_tups = tuple(player_list)
    query = f"select tournament_key,winner_id,p1_id,p2_id,p1_score,p2_score,location_names from sets where p1_id in {player_tups} and p2_id in {player_tups} and best_of is not null and p1_score >= 0 and p2_score >= 0"
    cur = conn.cursor()
    cur.execute(query)
    details = cur.fetchall()
    return details

def get_entrants_by_list_of_tournaments(tourney_list):
    tourney_tups = tuple(tourney_list)
    query = f"select tournament_info.key, entrants from tournament_info where tournament_info.key in {tourney_tups}"
    cur = conn.cursor()
    cur.execute(query)
    details = cur.fetchall()
    return details

def get_gamertag_by_idlist(_idlist):
    _id_tups = tuple(_idlist)
    query = f"select player_id, tag from players where player_id in {_id_tups}"
    cur = conn.cursor()
    cur.execute(query)
    details = cur.fetchall()
    return details