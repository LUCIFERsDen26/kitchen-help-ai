import requests
from flask import current_app
# Helper function to fetch nutrients
def fetch_nutrients(recipename):
    headers = {
        'Content-Type': 'application/json',
        'x-app-id': current_app.config['NutritionixAPI_applicationID'],
        'x-app-key': current_app.config['NutritionixAPI_applicationKEY']
    }
    body = {"query": recipename}
    
    response = requests.post('https://trackapi.nutritionix.com/v2/natural/nutrients', headers=headers, json=body)
    data = response.json()

    if "message" in data:
        return [{"Food Name": recipename, "Error": data["message"]}]

    nutrient_map = {
        203: "Protein",
        204: "Total Fat",
        205: "Total Carbohydrate",
        208: "Calories",
        291: "Dietary Fiber",
        305: "Phosphorus",
        306: "Potassium",
        307: "Sodium",
        601: "Cholesterol",
        606: "Saturated Fat",
        269: "Sugars",
    }

    nutrients = {"Food Name": recipename}
    for food in data.get("foods", []):
        for nutrient in food["full_nutrients"]:
            attr_id = nutrient["attr_id"]
            if attr_id in nutrient_map:
                nutrients[nutrient_map[attr_id]] = nutrient["value"]

    return nutrients