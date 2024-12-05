from flask import Blueprint, render_template, request
from Foodimg2Ing.utils.get_indg2recipe import get_indg2recipes
from Foodimg2Ing.utils.nutrientsUtils import fetch_nutrients
import os
import json
import re
ingd2Recipes = Blueprint('ingd2Recipe', __name__)


@ingd2Recipes.route('/searchByIngredients', methods=['GET','POST'])
def ingd2Recipe():
    """Handle get list of ingredients and return list of recipes."""
    recipes = []
    ingredientslist = []
    nutrients_data = []
    if request.method == 'POST':
        # Extract list of ingredients from the form
        ingredientslist = request.form.getlist('ingredients[]')
        
        data = json.loads(get_indg2recipes(ingredientslist))

        for key,value in data.items():
            #print(value)
            steps_list = re.split(r'\.\s(?=\d)', value['recipe_steps'])
            value['recipe_steps'] = steps_list
            recipes.append(value)

        # Process the recipes
        for recipe in recipes:
            
            nutrients = fetch_nutrients(recipe.get("recipe_title"))                
            nutrients_data.append({
                "recipe": recipe.get("recipe_title"),
                "nutrients": nutrients
        })       

        print(nutrients_data)

        return render_template("SearchByIngredents/output_SearchByIndgredents.html", recipes=recipes, ingredients=ingredientslist, nutrients_data=nutrients_data)

    return render_template("SearchByIngredents/searchByIndgredents.html")#, recipes=recipes, ingredients=ingredientslist)