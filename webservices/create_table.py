#!/usr/bin/python
import json
import collections
import sqlite3
from flask import Flask, jsonify, abort, request, make_response, url_for
conn = sqlite3.connect('black3js.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS game 
             (id integer primary key autoincrement, total_players int not null)''')
c.execute('''CREATE TABLE IF NOT EXISTS player 
             (id integer primary key autoincrement, game_id int not null, player varchar(5) not null)''')
c.execute('''CREATE TABLE IF NOT EXISTS score
             (id integer primary key autoincrement, game_id int not null, player_id int not null, score int default(0))''')


#c.execute("insert into game ('total_players') values ('5') ")
test = c.execute("select id, total_players from game")

objects_list = []
#print c.fetchall()

for row in  c.fetchall():
	d = collections.OrderedDict()
	d['id'] = row[0]
	d['total_players'] = row[1]
	objects_list.append(d)
 
j = json.dumps(objects_list)
print j

# Insert a row of data

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

