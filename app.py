from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for lists and tasks
lists = [
    {'id': 1, 'title': 'To Do', 'order': 1},
    {'id': 2, 'title': 'In Progress', 'order': 2},
    {'id': 3, 'title': 'Done', 'order': 3}
]

tasks = [
    {'id': 1, 'title': 'Task 1', 'description': 'Do something', 'due_date': '2023-05-01', 'order': 1, 'list_id': 1},
    {'id': 2, 'title': 'Task 2', 'description': 'Do something else', 'due_date': '2023-05-02', 'order': 2, 'list_id': 1},
    {'id': 3, 'title': 'Task 3', 'description': 'Do yet another thing', 'due_date': '2023-05-03', 'order': 1, 'list_id': 2},
    {'id': 4, 'title': 'Task 4', 'description': 'Do something different', 'due_date': '2023-05-04', 'order': 2, 'list_id': 2},
]

# Helper functions for finding lists and tasks by ID
def find_list(list_id):
    for l in lists:
        if l['id'] == list_id:
            return l
    return None

def find_task(task_id):
    for t in tasks:
        if t['id'] == task_id:
            return t
    return None

# API endpoints for lists
@app.route('/lists', methods=['GET'])
def get_lists():
    return jsonify(lists)

@app.route('/lists', methods=['POST'])
def create_list():
    new_list = {'id': len(lists) + 1, 'title': request.json['title'], 'order': request.json['order']}
    lists.append(new_list)
    return jsonify(new_list)

@app.route('/lists/<int:list_id>', methods=['GET'])
def get_list(list_id):
    l = find_list(list_id)
    if l:
        return jsonify(l)
    else:
        return jsonify({'error': 'List not found'}), 404

@app.route('/lists/<int:list_id>', methods=['PUT'])
def update_list(list_id):
    l = find_list(list_id)
    if l:
        l['title'] = request.json.get('title', l['title'])
        l['order'] = request.json.get('order', l['order'])
        return jsonify(l)
    else:
        return jsonify({'error': 'List not found'}), 404

@app.route('/lists/<int:list_id>', methods=['DELETE'])
def delete_list(list_id):
    l = find_list(list_id)
    if l:
        tasks_to_delete = [t for t in tasks if t['list_id'] == list_id]
        for t in tasks_to_delete:
            tasks.remove(t)
        lists.remove(l)
        return jsonify({'message': 'List and tasks deleted successfully'})
    else:
        return jsonify({'error': 'List not found'}), 404

@app.route('/lists/<int:list_id>/tasks', methods=['GET'])
def get_tasks(list_id):
    return jsonify([t for t in tasks if t['list_id'] == list_id])

# API endpoints for tasks
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = {
        'id': len(tasks) + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ''),
        'due_date': request.json.get('due_date', ''),
        'order': request.json.get('order', 1),
        'list_id': request.json['list_id']
    }
    tasks.append(new_task)
    return jsonify(new_task)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    t = find_task(task_id)
    if t:
        return jsonify(t)
    else:
        return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    t = find_task(task_id)
    if t:
        t['title'] = request.json.get('title', t['title'])
        t['description'] = request.json.get('description', t['description'])
        t['due_date'] = request.json.get('due_date', t['due_date'])
        t['order'] = request.json.get('order', t['order'])
        t['list_id'] = request.json.get('list_id', t['list_id'])
        return jsonify(t)
    else:
        return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    t = find_task(task_id)
    if t:
        tasks.remove(t)
        return jsonify({'message': 'Task deleted successfully'})
    else:
        return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>/move', methods=['PUT'])
def move_task(task_id):
    t = find_task(task_id)
    if t:
        new_list_id = request.json['list_id']
        if not find_list(new_list_id):
            return jsonify({'error': 'List not found'}), 404
        t['list_id'] = new_list_id
        return jsonify(t)
    else:
        return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>/reorder', methods=['PUT'])
def reorder_task(task_id):
    t = find_task(task_id)
    if t:
        new_order = request.json['order']
        t['order'] = new_order
        return jsonify(t)
    else:
        return jsonify({'error': 'Task not found'}), 404

app.run()