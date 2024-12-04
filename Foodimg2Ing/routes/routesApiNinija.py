import requests
from flask import Blueprint, render_template, request, current_app
from Foodimg2Ing.utils.nutrientsUtils import fetch_nutrients
# Create a Blueprint
recipeApi = Blueprint('recipeApi', __name__)

@recipeApi.route('/get_recipes', methods=['GET', 'POST'])
def get_recipes():
    
    recipes = []
    nutrients_data = []

    if request.method == 'POST':
        recipe_name = request.form.get('recipe_name')

        if recipe_name:
            api_url = f'https://api.api-ninjas.com/v1/recipe?query={recipe_name}'
            headers = {'X-Api-Key': current_app.config['API_NINJA_API_KEY']}
            response = requests.get(api_url, headers=headers)
            
            if response.status_code == requests.codes.ok and response.json() != []:
                recipes = response.json()
                
                for recipe in recipes:                
                    nutrients = fetch_nutrients(recipe.get("title"))                
                    nutrients_data.append({
                        "recipe": recipe.get("title"),
                        "nutrients": nutrients
                    })
                
            else:
                recipes = [{"Error":"no recipes found","title": "Error", "ingredients": "N/A", "instructions": "N/A"}]
            
    return render_template('apirecipesPages/getrecipes.html', recipes=recipes, nutrients_data=nutrients_data)
