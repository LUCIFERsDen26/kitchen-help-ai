from flask import Blueprint, render_template, request
from Foodimg2Ing.utils.get_indg2recipe import get_indg2recipes
import os
import json
ingd2Recipes = Blueprint('ingd2Recipe', __name__)
htmlPath = str(os.path.join("ingd2Recipe", "ingd2Recipe.html"))

@ingd2Recipes.route('/ingd2Recipe', methods=['GET','POST'])
def ingd2Recipe():
    """Handle get list of ingredients and return list of recipes."""
    recipes = []
    ingredients = []
    if request.method == 'POST':
        # Extract list of ingredients from the form
        ingredients = request.form.getlist('ingredients[]')
        print(ingredients)

        data = json.loads(get_indg2recipes(ingredients))

        for key,value in data.items():
            recipes.append(value)

    return render_template(htmlPath, recipes=recipes, ingredients=ingredients)