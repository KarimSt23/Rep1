from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated "database" (in-memory dictionary)
fake_db = {
    1: {'name': 'Alice', 'age': 30},
    2: {'name': 'Bob', 'age': 25}
}

@app.route('/')
def home():
    return "Welcome to the Flask app!"

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = fake_db.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    if 'name' not in data or 'age' not in data:
        return jsonify({"error": "Missing name or age"}), 400
    
    user_id = max(fake_db.keys()) + 1  # Generate new user ID
    fake_db[user_id] = {'name': data['name'], 'age': data['age']}
    return jsonify({"message": "User added", "user_id": user_id}), 201

@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = fake_db.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    if 'name' in data:
        user['name'] = data['name']
    if 'age' in data:
        user['age'] = data['age']
    
    return jsonify({"message": "User updated", "user": user})

if __name__ == '__main__':
    app.run(debug=True)
