from flask import jsonify, request, Response
from model import Food, db
from schema import FoodSchema
from flask_babel import _
import json

food_schema = FoodSchema()
foods_schema = FoodSchema(many=True)

def add_get_foods():
    if request.method == "POST":
       
        foods_title = request.json.get("title")
        foods_description = request.json.get("description")
        foods_picture = request.json.get("picture")
        foods_ingredients = request.json.get("ingredients")
        foods_category = request.json.get("category")
        foods_related = request.json.get("related")
        foods_وصف = request.json.get("وصف")

        new_food = Food(
            title=foods_title,
            description=foods_description,
            picture=foods_picture,
            ingredients=foods_ingredients,
            category=foods_category,
            related=foods_related,
            وصف=foods_وصف
        )

       
        db.session.add(new_food)
        db.session.commit()

        
        response_data = {
            "message": "تم انشاء القائمة",
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
            "category": food.category,
            "related": food.related,
            "وصف": food.وصف
        })

    
    response_data = {"foods": foods}
    json_data = json.dumps(response_data, ensure_ascii=False)
    response = Response(json_data, content_type='application/json; charset=utf-8')
    return response


def update_foods(food_id):
    food = Food.query.get(food_id)
  
    if food:
         
        foods_title = request.json["title"]
        foods_description = request.json.get("description", food.description)  
        foods_picture = request.json.get("picture", food.picture)  
        foods_ingredients=request.json.get("ingredients")
        foods_category=request.json.get("category")
        foods_related=request.json.get("related")
        foods_وصف=request.json.get("وصف")
        
        food.title = foods_title
        food.description = foods_description
        food.picture = foods_picture
        food.ingredients=foods_ingredients
        food.category=foods_category
        food.related =foods_related
        food.وصف=foods_وصف
        db.session.commit()
        return jsonify({"message": "تم تغيير القائمة"}), 200

 
def get_foods(food_id):
    food = Food.query.get(food_id)
    if food:
         
        return jsonify({
            "title": food.title,
            "description": food.description,
            "picture": food.picture,
            "ingredients": food.ingredients,
            "category": food.category,
            "related": food.related,
            "وصف": food.وصف
        })


def delete_foods(food_id):
    food = Food.query.get(food_id)
    if food:
        
        db.session.delete(food)
        db.session.commit()
        return jsonify({"message": "تم ازالة القائمة"}), 200
