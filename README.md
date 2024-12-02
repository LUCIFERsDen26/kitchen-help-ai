# Meal Mind

### Demo:
![Recipe_Generation gif](https://user-images.githubusercontent.com/55757415/124395585-8d0d0780-dd22-11eb-86fe-3a23d921b608.gif)


#### Ever found yourself staring at a delicious dish and wondering how to recreate it? With the Recipe Generation from Food Images application, simply snap a photo and let the system provide you with a detailed recipe.

### Overview:

This application utilizes deep learning to analyze food images and generate detailed cooking recipes. The system extracts key information from the image, such as:

    Recipe Title: A catchy name for the dish.
    Ingredients: A list of all the necessary ingredients.
    Instructions: Step-by-step cooking instructions for preparing the dish.

### Key Features:

- Advanced Deep Learning: State-of-the-art computer vision algorithms identify ingredients and cooking processes from food images.

- Natural Language Generation: Uses natural language processing to generate easy-to-follow cooking instructions from the analyzed data.

- Search by Image: Simply upload a photo of a dish, and the system will generate the recipe, identifying key ingredients and instructions.

- Search by Ingredients: Enter the ingredients you have, and the system will suggest recipes based on those items.

- Search by Recipe Name: Find recipes by entering the name of the dish and get detailed information, including ingredients and instructions.

- User-Friendly Interface: An intuitive web or mobile interface designed for a seamless user experience.

- Discover New Recipes: Explore a wide range of cuisines and dishes by simply taking pictures or entering ingredients.
---

### Prerequisite :
Download these files and replace it with the files in this folder "Foodimg2Ing/predictor/models"

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

You will be getting a localhost link and open that link in your browser 


