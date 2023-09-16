from flask import Flask,jsonify,request,Response
from controller import add_get_foods, update_foods, get_foods, delete_foods
from model import db
from database import DATABASE_URI 
from marshmallow import ValidationError
from flask_babel import Babel
from flask_babelex import Babel
import json


app = Flask(__name__)
babel = Babel(app)


app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False


db.init_app(app)


with app.app_context():
    db.create_all()


app.route("/foods", methods=["GET", "POST"])(add_get_foods)
app.route("/foods/<int:food_id>", methods=["PUT"])(update_foods)
app.route("/foods/<int:food_id>", methods=["GET"])(get_foods)
app.route("/foods/<int:food_id>", methods=["DELETE"])(delete_foods)




@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400

if __name__ == '__main__':
    app.run(debug=True)
    
    