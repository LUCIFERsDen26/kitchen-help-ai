import os
from flask import Flask
from dotenv import load_dotenv

def create_app():
    """Factory function to create and configure the Flask application."""
    # Load environment variables
    load_dotenv()

    app = Flask(__name__, template_folder='Templates')

    # Store the API key in app config
    app.config['API_NINJA_API_KEY'] = os.getenv('API-NINJA_KEY')
    app.config['NutritionixAPI_applicationID'] = os.getenv('NutritionixAPI_applicationID')
    app.config['NutritionixAPI_applicationKEY'] = os.getenv('NutritionixAPI_applicationKEY')

    # Import and register Blueprints
    #from Foodimg2Ing.routes.routesMain import main as main_blueprint
    from Foodimg2Ing.routes.routesApiNinija import recipeApi as recipeApi_blueprint
    from Foodimg2Ing.routes.routesNutrients import nutrients_api 
    from Foodimg2Ing.routes.routesIngd2Recipe import ingd2Recipes as ingd2Recipe_blueprint

    #app.register_blueprint(main_blueprint)
    app.register_blueprint(recipeApi_blueprint)
    app.register_blueprint(nutrients_api)
    app.register_blueprint(ingd2Recipe_blueprint)
    return app

