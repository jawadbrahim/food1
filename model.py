from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String(250)) 
    description = db.Column(db.Text)   
    picture = db.Column(db.String(500))
    ingredients = db.Column(db.String(1000)) 

    def __init__(self, title, description, picture, ingredients,id):
        self.title = title
        self.description = description
        self.picture = picture
        self.ingredients = ingredients
        self.id=id
