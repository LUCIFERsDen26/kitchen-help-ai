import os
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_schema": content.Schema(
    type = content.Type.OBJECT,
    enum = [],
    required = ["recipe_1", "recipe_2", "recipe_3"],
    properties = {
      "recipe_1": content.Schema(
        type = content.Type.OBJECT,
        enum = [],
        required = ["recipe_title", "recipe_indgredents", "recipe_steps"],
        properties = {
          "recipe_title": content.Schema(
            type = content.Type.STRING,
          ),
          "recipe_indgredents": content.Schema(
            type = content.Type.STRING,
          ),
          "recipe_steps": content.Schema(
            type = content.Type.STRING,
          ),
        },
      ),
      "recipe_2": content.Schema(
        type = content.Type.OBJECT,
        enum = [],
        required = ["recipe_title", "recipe_indgredents", "recipe_steps"],
        properties = {
          "recipe_title": content.Schema(
            type = content.Type.STRING,
          ),
          "recipe_indgredents": content.Schema(
            type = content.Type.STRING,
          ),
          "recipe_steps": content.Schema(
            type = content.Type.STRING,
          ),
        },
      ),
      "recipe_3": content.Schema(
        type = content.Type.OBJECT,
        enum = [],
        required = ["recipe_title", "recipe_indgredents", "recipe_steps"],
        properties = {
          "recipe_title": content.Schema(
            type = content.Type.STRING,
          ),
          "recipe_indgredents": content.Schema(
            type = content.Type.STRING,
          ),
          "recipe_steps": content.Schema(
            type = content.Type.STRING,
          ),
        },
      ),
    },
  ),
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="Role Definition:\n\n    Role: You are an AI Kitchen Helper.\n    Purpose: To provide a list of possible recipe names based on available main ingredients.\n    Output Requirement:  Only list of recipes in given format nothing more.\n\nInput Rules:\n\n    Ingredient List:\n    You will receive a list of available main ingredients in the kitchen.\n    Example input:\n        \"paneer, chicken, spinach\"\n\nOutput Rules:\n\n    Original & Authentic Recipes Only:\n        Provide names of recipes that strictly adhere to traditional or widely recognized versions.\n        Do not include any variations or fusion dishes.\n\n    Example:\n        Correct: \"Paneer Tikka, Butter Chicken\"\n        Incorrect: \"Paneer Tikka Masala (variation), Spicy Butter Chicken (variation)\"\n\n    Separate Recipes for Each Ingredient:\n        If more than one main ingredient is found, suggest one distinct recipe for each ingredient, not combinations.\n        Example input: \"paneer, chicken\"\n        Output: \"Paneer Tikka, Butter Chicken\"\n\n    No Additional Explanations or Ingredients:\n        Output only the recipe names in a comma-separated format. No explanations, descriptions, or additional information.\n\n    Single Focus Recipes:\n        Each recipe should center around only one of the given main ingredients.\n        No mixed-ingredient recipes unless explicitly allowed.\n\nExample Instructions and Responses:\n\n    Instruction:\n    \"potato, eggplant, fish\"\n\n    Output:\n    \"Aloo Gobi, Baingan Bharta, Grilled Fish\"\n\n    Instruction:\n    \"chicken, mutton\"\n\n    Output:\n    \"Chicken Curry, Mutton Biryani\"",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Spinach, pumpkin, Dill, curd, milk, panner",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"recipe_1\": {\"recipe_indgredents\": \"1 pound fresh spinach, 1 tablespoon olive oil, 2 cloves garlic, minced, 1/4 teaspoon salt, 1/4 teaspoon black pepper\", \"recipe_steps\": \"1. Wash and drain the spinach thoroughly. 2. Heat the olive oil in a large skillet over medium heat. Add the garlic and cook for about 30 seconds, until fragrant. 3. Add the spinach to the skillet and cook until wilted, about 2-3 minutes. 4. Season with salt and pepper to taste.\", \"recipe_title\": \"Sauteed Spinach\"}, \"recipe_2\": {\"recipe_indgredents\": \"1 small pumpkin (about 2 pounds), 1 tablespoon olive oil, 1/2 teaspoon salt, 1/4 teaspoon black pepper\", \"recipe_steps\": \"1. Preheat oven to 400°F (200°C). 2. Cut the pumpkin in half and remove the seeds and stringy pulp. 3. Drizzle the cut sides of the pumpkin with olive oil and season with salt and pepper. 4. Place the pumpkin halves cut-side down on a baking sheet and bake for about 45-60 minutes, or until tender when pierced with a fork.\", \"recipe_title\": \"Roasted Pumpkin\"}, \"recipe_3\": {\"recipe_indgredents\": \"1 cup fresh dill, 1/4 cup olive oil, 2 tablespoons lemon juice, 1/4 teaspoon salt, 1/4 teaspoon black pepper\", \"recipe_steps\": \"1. Combine all ingredients in a blender or food processor and pulse until smooth.\", \"recipe_title\": \"Dill Sauce\"}}\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        "eggplant, drum sticks, oinon",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"recipe_1\": {\"recipe_indgredents\": \"1 large eggplant, 1 tablespoon olive oil, 1/2 teaspoon salt, 1/4 teaspoon black pepper\", \"recipe_steps\": \"1. Preheat oven to 400°F (200°C). 2. Prick the eggplant all over with a fork. 3. Place the eggplant on a baking sheet and bake for about 45-60 minutes, or until tender when pierced with a fork. 4. Let the eggplant cool slightly, then scoop out the flesh and mash it with a fork. 5. Season with salt and pepper to taste.\", \"recipe_title\": \"Roasted Eggplant\"}, \"recipe_2\": {\"recipe_indgredents\": \"1 pound chicken drumsticks, 1 tablespoon olive oil, 1/2 teaspoon salt, 1/4 teaspoon black pepper\", \"recipe_steps\": \"1. Preheat oven to 400°F (200°C). 2. Place the drumsticks on a baking sheet and drizzle with olive oil. 3. Season with salt and pepper to taste. 4. Bake for about 30-40 minutes, or until cooked through.\", \"recipe_title\": \"Baked Chicken Drumsticks\"}, \"recipe_3\": {\"recipe_indgredents\": \"1 large onion, thinly sliced, 1 tablespoon olive oil, 1/4 teaspoon salt, 1/4 teaspoon black pepper\", \"recipe_steps\": \"1. Heat the olive oil in a large skillet over medium heat. 2. Add the onion and cook until softened and caramelized, about 15-20 minutes. 3. Season with salt and pepper to taste.\", \"recipe_title\": \"Caramelized Onions\"}}\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        "ghevda, bhopala,  Ivy-gourd, panner\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"recipe_1\": {\"recipe_indgredents\": \"1 cup ghevda, 1/2 cup sugar, 1/4 cup water\", \"recipe_steps\": \"1. Combine the ghevda, sugar, and water in a saucepan over medium heat. 2. Bring to a boil, then reduce heat and simmer for 10-15 minutes, or until the ghevda is soft. 3. Serve hot or cold.\", \"recipe_title\": \"Ghevda Kheer\"}, \"recipe_2\": {\"recipe_indgredents\": \"1 cup bhopala, 1/2 cup sugar, 1/4 cup water\", \"recipe_steps\": \"1. Combine the bhopala, sugar, and water in a saucepan over medium heat. 2. Bring to a boil, then reduce heat and simmer for 10-15 minutes, or until the bhopala is soft. 3. Serve hot or cold.\", \"recipe_title\": \"Bhopala Kheer\"}, \"recipe_3\": {\"recipe_indgredents\": \"1 cup ivy gourd, 1 tablespoon oil, 1/2 teaspoon salt, 1/4 teaspoon black pepper\", \"recipe_steps\": \"1. Heat the oil in a skillet over medium heat. 2. Add the ivy gourd and cook until tender, about 5-7 minutes. 3. Season with salt and pepper to taste.\", \"recipe_title\": \"Sauteed Ivy Gourd\"}}\n```",
      ],
    },
  ]
)

def get_indg2recipes(indgredents):
    response = chat_session.send_message(indgredents)
    return response.text