""" This file is used for creating a routes """

from flask import Blueprint
from app.controllers.home_controller import index, get_distance

home_blueprint = Blueprint("main", __name__)

home_blueprint.route('/', methods=['GET'])(index)
home_blueprint.route('/get-distance', methods=['POST'])(get_distance)
