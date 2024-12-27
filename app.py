from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store (for simplicity)
users = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25}
]

# Create a user
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        "id": len(users) + 1,
        "name": data['name'],
        "age": data['age']
    }
    users.append(new_user)
    return jsonify({"message": "User added", "user_id": new_user["id"]}), 201

# Read users
@app.route('/user', methods=['GET'])
def get_users():
    return jsonify(users)

# Update a user
@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        user["name"] = data["name"]
        user["age"] = data["age"]
        return jsonify({"message": "User updated"})
    else:
        return jsonify({"message": "User not found"}), 404

# Delete a user
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run(debug=True)
