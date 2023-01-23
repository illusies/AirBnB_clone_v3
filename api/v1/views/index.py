#!/usr/bin/python3
"""
Index of the views package to connect to API
"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage


classes = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
}


@app_views.route("/status", strict_slashes=False)
def hbnbStatus():
    """ return a JSON status ok """
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def hbnbStats():
    """ retrieves the number of each objects by type """
    return_dict_obj = {}
    for key, value in classes.items():
        return_dict_obj[key] = storage.count(value)
    return jsonify(return_dict_obj)
