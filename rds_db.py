# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:34:18 2020
@author: hp
"""

import pymysql
conn = pymysql.connect(
    host = "panda-local.cmcngdzhrbgb.us-east-2.rds.amazonaws.com",
    port = 3306,
    user = "admin",
    password = "advaitejaeric",
    database = "smash"
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


def get_player_by_gamertag(tag):
    query = f"SELECT * FROM Player WHERE gamer_tag = '{tag}'"
    cur=conn.cursor()
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
    query = f"DELETE FROM Player WHERE gamer_tag = '{tag}' AND scraped = 'F'"
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