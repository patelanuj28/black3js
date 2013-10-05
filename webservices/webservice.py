#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
from sql_database import *

app = Flask(__name__, static_url_path = "")

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

    
@app.route('/todo/api/v1.0/tasks', methods = ['GET'])
def get_tasks():
    tasks = get_gameAll()
    return tasks

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['GET'])
def get_task(task_id):
    task = get_gameAll(task_id)
    
    if len(task) == 0:
        abort(404)
    return task

@app.route('/todo/api/v1.0/tasks', methods = ['POST'])
def create_task():
    if not request.json or not 'total_players' in request.json:
        abort(400)
    test = insert_game(request.json['total_players'])
    return jsonify( test ), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['PUT'])
def update_task(task_id):    
    if task_id == 0 or task_id == '':
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['total_players']) != unicode:
        abort(400)
    
    test = update_game(task_id, request.json['total_players'])
    
    return jsonify( test )
    
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['DELETE'])
def delete_task(task_id):
    if task_id == '':
        abort(404)
    tid = task_id
    test = delete_game(tid)
    return jsonify( test )
    
if __name__ == '__main__':
    app.run(debug = True)
