# BiteBlueprint

#### Ever found yourself staring at a delicious dish and wondering how to recreate it? With the Recipe Generation from Food Images application, simply snap a photo and let the system provide you with a detailed recipe.

### Overview:

This application leverages deep learning and AI to analyze food images, generate detailed cooking recipes, and provide intelligent culinary insights. The system processes input to extract and deliver key information, including:

Recipe Title: The name of the identified dish.
Ingredients: A comprehensive list of required ingredients.
Instructions: Clear, step-by-step cooking directions for preparing the dish.
In addition to image-based recognition, the application offers:

Text-Based Recipe Search: Users can input a dish name to instantly access its recipe and ingredient details.
Ingredient-Based Suggestions: Users can list available ingredients to receive recipe recommendations tailored to what they have on hand.
Nutritional Information: Displays detailed nutritional insights for each recipe, helping users make informed dietary choices.
Interactive User Interface: Features intuitive tabs for easy navigation and seamless access to functionalities.
Customizable Recipes: Users can adjust ingredient quantities and serving sizes to suit their preferences.

### Key Features:

-Snap, Upload, Discover: Upload a food image to identify it, get ingredients, and view a step-by-step recipe.

-Name it, Make it: Input a dish name to instantly access its recipe and ingredient list.

-Turn Ingredients into Magic: Enter available ingredients to get recipe suggestions with nutritional values.

-Interactive User Interface: User-friendly tabs for seamless navigation between features.

-Nutrition Insights: Provides comprehensive nutrition details for each suggested recipe.

-Smart Suggestions: Suggests creative recipes based on the ingredients available.

-Efficient and Accurate Identification: Uses AI/ML for accurate food recognition and tailored recipes.

-Customizable Outputs: Allows ingredient adjustments and serving size customization for personalized recipes.

---

### Prerequisite :

Download these files and replace it with the files in this folder "Foodimg2Ing\predictor\models\"

1. Model (Modelbest.ckpt) : [Download Modelbest.ckpt](https://dl.fbaipublicfiles.com/inversecooking/modelbest.ckpt)

2. Ingredients (ingr_vocab.pkl) : [Download ingr_vocab.pkl](https://dl.fbaipublicfiles.com/inversecooking/ingr_vocab.pkl)

3. Instruction (instr_vocab.pkl) : [Download instr_vocab.pkl](https://dl.fbaipublicfiles.com/inversecooking/instr_vocab.pkl)

### To run the Code :

1. Open Terminal (cmd)

2. Create Virtule Enviroment by
   ```bash
   pytohn3 -m venv venv
   ```
3. Install all the required libraries using
   ```bash
   pip install -r requirements.txt
   ```
4. run
   ```bash
   python run.py
   ```
