from flask import Flask,request
from controller import add_get_foods, update_foods, get_foods, delete_foods
from model import db
from main import app
@app.route("/food", methods=["POST", "GET"])
def foods():
    return add_get_foods()

@app.route("/foods/<int:food_id>", methods=["PUT", "GET", "DELETE"])
def food(food_id):
    if request.method == "PUT":
        return update_foods(food_id)
    elif request.method == "GET":
        return get_foods(food_id)
    elif request.method == "DELETE":
        return delete_foods(food_id)
