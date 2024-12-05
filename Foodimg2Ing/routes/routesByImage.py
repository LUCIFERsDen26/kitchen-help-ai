import os
from flask import Blueprint, render_template, request
from Foodimg2Ing.predictor.output import output
from Foodimg2Ing.utils.nutrientsUtils import fetch_nutrients
# Create a Blueprint
main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    """Render the home page or handle image upload and prediction based on the request method."""
    
    if request.method == 'GET':
        # Render the home page
        return render_template('SearchByImage/searchByImage.html')
    
    elif request.method == 'POST':
        # Handle image upload and prediction
        imagefile = request.files['imagefile']
        image_path = os.path.join(os.getcwd(), 'Foodimg2Ing','static','uploadedImages', imagefile.filename)
        
        imagefile.save(image_path)

        img = f"uploadedImages/{imagefile.filename}"
        
        recipes = output(image_path)

        nutrients_data = []
        # Process the recipes
        for recipe in recipes:            
            nutrients = fetch_nutrients(recipe['title'])
            nutrients_data.append({
                "recipe": recipe['title'],
                "nutrients": nutrients
        })       
            
        # print('-------------------------------')
        # print(nutrients_data, end='\n\n')
        # print(recipes)
        # print('-------------------------------')

        return render_template('SearchByImage/output_SearchByImage.html',recipes=recipes, img=img, nutrients_data=nutrients_data)

@main.route('/about', methods=['GET'])
def about():
    """Render the about page."""
    return render_template('about.html')


@main.route('/<samplefoodname>')
def predict_sample(samplefoodname):
    """Predict recipe based on a sample image filename."""
    imagefile = os.path.join(os.getcwd(), 'Foodimg2Ing/static/images', f"{samplefoodname}.jpg")
    img = f"/images/{samplefoodname}.jpg"
    
    recipes = output(imagefile)

    nutrients_data = []
    # Process the recipes
    for recipe in recipes:            
        nutrients = fetch_nutrients(recipe['title'])
        nutrients_data.append({
            "recipe": recipe['title'],
            "nutrients": nutrients
    })       
        
    # print('-------------------------------')
    # print(nutrients_data, end='\n\n')
    # print(recipes)
    # print('-------------------------------')
    return render_template('SearchByImage/output_SearchByImage.html',recipes=recipes, img=img, nutrients_data=nutrients_data)