#!/usr/bin/python3
"""contains status and stat endpoints"""
from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


@app_views.route("/status")
def status():
    """API Status"""
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def stats():
    """Retrieve the number of each objects by type"""
    retrieved = {}

    for key, value in classes.items():
        retrieved[key] = storage.count(value)

    return jsonify(retrieved)
