from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

@app.route('/', methods=['POST'])
def create():
    data = request.get_json()
    print(data)
    return jsonify({'message': 'Created'})