#!/usr/bin/python3
"""
getting start with the api
"""
from os import getenv
from flask import Flask, jsonify
from flask_cors import CORS
from api.v1.views import app_views
from models import storage


app = Flask(__name__)
app_host = getenv('HBNB_API_HOST', '0.0.0.0')
app_port = int(getenv('HBNB_API_PORT', '5000'))
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
CORS(app, resources={'/*': {'origins': app_host}})


@app.teardown_appcontext
def teardown_flask(exception):
    '''flask leastner to handle exception'''
    storage.close()


@app.errorhandler(404)
def error_404(error):
    '''Handle not founded pages'''
    return jsonify(error='Not found'), 404


@app.errorhandler(400)
def error_400(error):
    '''Handle error handler'''
    output = 'Bad request'
    if isinstance(error, Exception) and hasattr(error, 'description'):
        output = error.description
    return jsonify(error=output), 400


if __name__ == '__main__':
    app_host = getenv('HBNB_API_HOST', '0.0.0.0')
    app_port = int(getenv('HBNB_API_PORT', '5000'))
    app.run(
        host=app_host,
        port=app_port,
        threaded=True
    )
