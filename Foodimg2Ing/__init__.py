import os
from flask import Flask
from dotenv import load_dotenv
def create_app():
    """Factory function to create and configure the Flask application."""
    app = Flask(__name__, template_folder='Templates')
    load_dotenv()
    app.config['API_NINJA_API_KEY'] = os.getenv('API_NINJA_API_KEY')
    app.config['NutritionixAPI_applicationID'] = os.getenv('NutritionixAPI_applicationID')
    app.config['NutritionixAPI_applicationKEY'] = os.getenv('NutritionixAPI_applicationKEY')
    
    # Import and register Blueprints
    from Foodimg2Ing.routes import main as main_blueprint

    app.register_blueprint(main_blueprint)


    return app
