import os
from flask import Blueprint, render_template, request
from Foodimg2Ing.predictor.output import output

# Create a Blueprint
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
    """Handle image upload and prediction."""
    imagefile = request.files['imagefile']
    image_path = os.path.join(os.getcwd(), 'Foodimg2Ing/static/demo_imgs', imagefile.filename)
    
    imagefile.save(image_path)

    img = f"/demo_imgs/{imagefile.filename}"
    
    title, ingredients, recipe = output(image_path)

    return render_template('search-by-image_predict.html', title=title, ingredients=ingredients, recipe=recipe, img=img)

@main.route('/<samplefoodname>')
def predict_sample(samplefoodname):
    """Predict recipe based on a sample image filename."""
    imagefile = os.path.join(os.getcwd(), 'Foodimg2Ing/static/images', f"{samplefoodname}.jpg")
    img = f"/images/{samplefoodname}.jpg"
    
    title, ingredients, recipe = output(imagefile)

    return render_template('search-by-image_predict.html', title=title, ingredients=ingredients, recipe=recipe, img=img)