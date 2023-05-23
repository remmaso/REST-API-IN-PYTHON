# Create a REST API in python  it should run on port 3000, and the end point should be implemented 

#  example of a simple REST API in Python using the Flask framework. It runs on port 3000 and has a single endpoint /hello that returns a JSON response with a greeting.

# To run this code, you'll need to install Flask if you haven't already. You can install it using pip:
# pip install flask

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, world!'})

if __name__ == '__main__':
    app.run(port=3000)
