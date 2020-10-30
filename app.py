# import the Flask class from the flask module
from flask import Flask, render_template, request, jsonify
import os

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url


@app.route('/')
def home():
    app.logger.info(' logged in successfully')
    return "Hello, World!"  # return a string


@app.route('/health')
def health():
    return 'OK'


@app.route('/devhose', methods=['POST'])
def create_app():

    data = request.json
    app.logger.info(request.get_json(force=True))
    return jsonify(data), 201


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
