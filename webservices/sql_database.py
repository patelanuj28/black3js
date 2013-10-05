import json
import collections
import sqlite3
from flask import Flask, jsonify, abort, request, make_response, url_for


def insert_game(play = ''):
    if play == '':
        abort(404)

    conn = sqlite3.connect('black3js.db')
    c = conn.cursor()
    try:
        with conn:
            conn.execute("insert into game(total_players) values (?)", play )
            return ({'success' : 'Game created successfully.'})
    except sqlite3.IntegrityError:
        return ({'error' : 'New game creation failed' })

def delete_game(tid = ''):
    if tid == '':
        abort(404)
    conn = sqlite3.connect('black3js.db')
    c = conn.cursor()
    try:
        with conn:
            conn.execute("delete from game where id= '%s'" % tid)
            return ({'success' : 'Game deleted successfully.'})
    except sqlite3.IntegrityError:
        return ({'error' : 'Game deletion failed' })


def update_game(game_id, play =''):
    if play == '' and game_id == '':
        abort(404)

    conn = sqlite3.connect('black3js.db')
    c = conn.cursor()
    try:
        with conn:
            conn.execute("update game set total_players =? where id =?",(play,game_id ))
            return ({'success' : 'Game update successfully.'})
    except sqlite3.IntegrityError:
        return ({'error' : 'failed to update game' })


def get_gameAll(task_id = ''):
    where = ''
    if task_id:
        where = ' where id="'+ str(task_id) + '"'
    conn = sqlite3.connect('black3js.db')
    c = conn.cursor()
    c.execute("select id, total_players from game" + where)
    objects_list = []
    
    count = 0
    for row in  c.fetchall():
        d = collections.OrderedDict()
        d['id'] = row[0]
        d['total_players'] = row[1]
        objects_list.append(d)
        count = count +1 
    

    j = json.dumps(objects_list)

    if count == 0:
        abort(404)

    return j
