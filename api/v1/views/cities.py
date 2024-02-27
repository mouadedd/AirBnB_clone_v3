#!/usr/bin/python3
"""Handle RESTful API for City"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State
from models.city import City


@app_views.route("/states/<state_id>/cities")
def cities_in_state(state_id):
    """Retrieve the list of all Citys in astate"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)

    output = []
    for city in state.cities:
        output.append(city.to_dict())
    return jsonify(output)


@app_views.route("/cities/<city_id>")
def city(city_id):
    """Retrieve the City in db"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route("/cities/<city_id>", methods=["DELETE"])
def delete_city(city_id):
    """ delete  a city """
    city = storage.get(City, city_id)
    if not city:
        abort(404)

    city.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route("/states/<state_id>/cities", methods=["POST"])
def create_city(state_id):
    """ Create a city """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    if "name" not in request.get_json():
        abort(400, "Missing name")

    city = City(state_id=state_id, **request.get_json())
    city.save()
    return jsonify(city.to_dict()), 201


@app_views.route("/cities/<city_id>", methods=["PUT"])
def update_city(city_id):
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    name = "name"
    setattr(city, name, request.get_json().get(key))
    city.save()

    return jsonify(city.to_dict())
