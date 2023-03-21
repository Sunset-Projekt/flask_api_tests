from app import app, db
from flask import render_template, jsonify, request, abort
from .models import Task


@app.route("/")
def index():
    return render_template("welcome.html")


@app.route("/api/tasks", methods = ['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([item.serialize() for item in tasks])


@app.route("/api/tasks/<int:task_id>", methods = ['GET'])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify(task.serialize())


@app.route('/api/tasks/', methods = ['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = Task(title=request.json['title'], description=request.json.get('description', ""))
        
    db.session.add(task)
    db.session.commit()

    return jsonify(task.serialize()), 201


@app.route('/api/tasks/<int:task_id>', methods = ['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    if not request.json:
        abort(400)
    task.title = request.json.get('title', task.title)
    task.description = request.json.get('description', task.description)
    db.session.add(task)
    db.session.commit()
    return jsonify(task.serialize())

@app.route('/api/tasks/<int:task_id>', methods = ['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'success': True})