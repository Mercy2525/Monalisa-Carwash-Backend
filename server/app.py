from flask import Flask
from flask_migrate import Migrate
from models import db, Appointment, Product, Feedback 

from flask_restful import Api, Resource


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

migrate=Migrate(app,db)
db.init_app(app)

api=Api(app)