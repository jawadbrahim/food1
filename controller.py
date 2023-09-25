from flask import jsonify, request, Response
from model import Food, db
from schema import FoodSchema
from flask_babel import _
import json

food_schema = FoodSchema()
foods_schema = FoodSchema(many=True)

def add_get_foods():
    if request.method == "POST":
       
        food_id = request.json.get("id")
        foods_title = request.json.get("title")
        foods_description = request.json.get("description")
        foods_picture = request.json.get("picture")
        foods_ingredients = request.json.get("ingredients")
        
        
        existing_food = Food.query.get(food_id)

        if existing_food:
            existing_food.title = foods_title
            existing_food.description = foods_description
            existing_food.picture = foods_picture
            existing_food.ingredients = foods_ingredients
        else:
            
            new_food = Food(
                id=food_id,  
                title=foods_title,
                description=foods_description,
                picture=foods_picture,
                ingredients=foods_ingredients,
            )
            db.session.add(new_food)

        db.session.commit()

        response_data = {
            "message": "created succefuly",
        }
        json_data = json.dumps(response_data, ensure_ascii=False)
        response = Response(json_data, content_type='application/json; charset=utf-8')
        return response, 201

    
    foods_list = Food.query.all()
    foods = []

    for food in foods_list:
        foods.append({
            "title": food.title,
            "description": food.description,
            "picture": food.picture,
            "ingredients": food.ingredients,
            
        })

    
    response_data = {"foods": foods}
    json_data = json.dumps(response_data, ensure_ascii=False)
    response = Response(json_data, content_type='application/json; charset=utf-8')
    return response


def update_foods(food_id):
    
    foods_title = request.json["title"]
    foods_description = request.json.get("description")
    foods_picture = request.json.get("picture")
    foods_ingredients = request.json.get("ingredients")

    food = Food.query.get(food_id)

    if not food:
        
        return jsonify({"message": "Food not found"}), 404

    
    food.title = foods_title
    food.description = foods_description
    food.picture = foods_picture
    food.ingredients = foods_ingredients

    
    db.session.commit()

    
    return jsonify({"message": "update succefuly"}), 200


 
def get_foods(food_id):
    food = Food.query.get(food_id)
    if food:
         
        return jsonify({
            "title": food.title,
            "description": food.description,
            "picture": food.picture,
            "ingredients": food.ingredients,
            
        })


def delete_foods(food_id):
    food = Food.query.get(food_id)
    if food:
        
        db.session.delete(food)
        db.session.commit()
        return jsonify({"message": "delete succefuly"}), 200
