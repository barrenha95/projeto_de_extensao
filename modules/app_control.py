from flask import Flask, jsonify

app = Flask(__name__);

@app.route('/users', methods=['GET'])
def get_users():
  return jsonify([
        {'id': 546, 'username': 'John'},
        {'id': 894, 'username': 'Mary'},
        {'id': 326, 'username': 'Jane'}
    ])


@app.route('/users', methods=['DELETE'])
def delete_user():
    return jsonify({'result': 'success'})

app.run()

# http://127.0.0.1:5000/users