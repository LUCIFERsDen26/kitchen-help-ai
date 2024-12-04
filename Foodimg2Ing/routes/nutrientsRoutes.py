# nutrientsRoutes.py
from flask import Blueprint, current_app, jsonify
from Foodimg2Ing.utils.nutrientsUtils import fetch_nutrients

nutrients_api = Blueprint('nutrients_api', __name__)

@nutrients_api.route('/get_nutrients/<recipename>')
def get_nutrients(recipename):

    recipenutrients = fetch_nutrients(recipename)   

    return jsonify(recipenutrients)
