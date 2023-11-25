from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    __tablename__='products'

    id = db.Column(db.Integer, primary_key=True)

    product_name=db.Column(db.String)
    cost=db.Column(db.Integer)
    image=db.Column(db.String)


class Appointment(db.Model):
    __tablename__='appointments'

    id = db.Column(db.Integer, primary_key=True)

    full_name=db.Column(db.String)
    email=db.Column(db.String)
    phonenumber=db.Column(db.String)
    message= db.Column(db.String)
    service = db.Column(db.String)
    vehicle_make= db.Column(db.String)
    vehicle_model= db.Column(db.Integer)
    appointment_date=db.Column(db.DateTime, default=db.func.current_timestamp())
    time_frame= db.Column(db.String)

class Feedback(db.Model):
    __tablename__='feedbacks'

    id = db.Column(db.Integer, primary_key=True)

    full_name=db.Column(db.String)
    email=db.Column(db.String)
    phonenumber=db.Column(db.String)
    message= db.Column(db.String)
    vehicle_make= db.Column(db.String)
    vehicle_no= db.Column(db.Integer)
    
    service = db.Column(db.String)
    appointment_date= db.Column(db.DateTime, onupdate=db.func.current_timestamp())



