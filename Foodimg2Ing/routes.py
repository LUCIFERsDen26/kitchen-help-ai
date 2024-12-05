import os
import requests
import json
from flask import Blueprint, render_template, request, jsonify,current_app
from Foodimg2Ing.predictor.output import output
from Foodimg2Ing.utils.nutrientsUtils import fetch_nutrients
from Foodimg2Ing.utils.get_indg2recipe import get_indg2recipes

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    """Render the home page."""
    return render_template('home.html')

@main.route('/about', methods=['GET'])
def about():
    """Render the about page."""
    return render_template('about.html')

@main.route('/', methods=['POST'])
def predict():
    """Handle input from text, image, or ingredients."""
    # Case 1: Image upload
    if 'imagefile' in request.files:
        nutrients_data = []
        imagefile = request.files['imagefile']
        image_path = os.path.join(os.getcwd(), 'Foodimg2Ing\\static\\demo_imgs', imagefile.filename)
        imagefile.save(image_path)
        img = f"\\demo_imgs\\{imagefile.filename}"
        img2 = f"\\static\\demo_imgs\\{imagefile.filename}"
        title, ingredients, recipe = output(image_path)

        for thetitle in title:
            nutrients = fetch_nutrients(thetitle)
            nutrients_data.append({
                    "recipe": thetitle,
                    "nutrients": nutrients})
            
        return render_template('search-by-image_predict.html', title=title, ingredients=ingredients, recipe=recipe, img=img2,nutrients_data=nutrients_data)
    
    # Case 2: Dish name input
    elif 'recipe_name' in request.form:
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
                            "nutrients": nutrients})
                
                else:
                    recipes = [{"Error":"no recipes found","title": "Error", "ingredients": "N/A", "instructions": "N/A"}]
        
        return render_template('getrecipes.html', recipes=recipes, nutrients_data=nutrients_data)
    
    # Case 3: Ingredients input
    elif 'ingridientlist' in request.form:
        ingridientlist = request.form.get('ingridientlist').split(',')
        recipes = []
        data = json.loads(get_indg2recipes(ingridientlist))
        recipesname = []
        for key,value in data.items():
            recipes.append(value)
        
        for entry in recipes:
            recipesname.append(entry.get("recipe_title"))

        nutrients_data = []
        for recipe_title in recipesname:                
            nutrients = fetch_nutrients(recipe_title)                
            nutrients_data.append({
                "recipe": recipe_title,
                "nutrients": nutrients
            })


        return render_template('ingd2Recipe.html',recipes=recipes, ingredients=ingridientlist, nutrients_data=nutrients_data)

    else:
        return jsonify({'error': 'Invalid input'}), 400