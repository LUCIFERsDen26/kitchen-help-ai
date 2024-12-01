from flask import Flask

def create_app():
    """Factory function to create and configure the Flask application."""
    app = Flask(__name__, template_folder='Templates')
    
    # Import and register Blueprints
    from Foodimg2Ing.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
