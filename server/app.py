from flask import Flask,make_response,jsonify, request
from flask_migrate import Migrate
from models import db, Appointment, Product, Feedback 

from flask_restful import Api, Resource


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

migrate=Migrate(app,db)
db.init_app(app)

api=Api(app)

class ProductResource(Resource):
    def get(self):
        products = [product.to_dict() for product in Product.query.all()]
        
        response= make_response(jsonify(products), 200)
        return response
    
    def post(self):
        new_product =Product(
            product_name=request.get_json()['product_name'],
            cost=request.get_json()['cost'],
            image= request.get_json()['image']
        )

        db.session.add(new_product)
        db.session.commit()

        user_dict = new_product.to_dict()

        response = make_response(jsonify(user_dict), 201)

        return response

class ProductById(Resource):
    def get(self,id):        
        product = Product.query.filter_by(id=id).first().to_dict()

        response = make_response(jsonify(product), 201)
        response.headers["Content-Type"]= "application/json"

        return response
        
    def patch(self,id):
        product = Product.query.filter_by(id=id).first()

        for attr in request.get_json():
            setattr(product, attr, request.get_json()[attr])

        db.session.add(product)
        db.session.commit()

        product_dict = product.to_dict()

        response = make_response(jsonify(product_dict), 201)

        return response

    def delete(self,id):
                        
        product = Product.query.filter_by(id=id).first()
        db.session.delete(product)
        db.session.commit()

        response_dict = {
            "delete_successful": True,
            "message": "Product deleted."    
        }

        response = make_response(jsonify(response_dict), 201)
        return response

class AppointmentResource(Resource):
    def get(self):
        appointments = [appointment.to_dict() for appointment in Appointment.query.all()]
        
        response= make_response( jsonify(appointments), 200)

        return response
    
    def post(self):
        new_appointment =Appointment(
            full_name=request.get_json()['full_name'],
            email=request.get_json()['email'],
            phonenumber= request.get_json()['phonenumber'],
            message=request.get_json()['message'],
            service=request.get_json()['service'],
            vehicle_make=request.get_json()['vehicle_make'],
            time_frame=request.get_json()['time_frame'],
            vehicle_model=request.get_json()['vehicle_model']
        )

        db.session.add(new_appointment)
        db.session.commit()

        appointment_dict = new_appointment.to_dict()

        response = make_response(jsonify(appointment_dict), 201)

        return response
    

class AppointmentById(Resource):
    def get(self,id):        
        appointment = Appointment.query.filter_by(id=id).first().to_dict()

        response = make_response(jsonify(appointment), 201)
        response.headers["Content-Type"]= "application/json"

        return response
        
    def patch(self,id):
        appointment = Appointment.query.filter_by(id=id).first()

        for attr in request.get_json():
            setattr(appointment, attr, request.get_json()[attr])

        db.session.add(appointment)
        db.session.commit()

        appointment_dict = appointment.to_dict()

        response = make_response(jsonify(appointment_dict), 201)

        return response

    def delete(self,id):     
        appointment = Appointment.query.filter_by(id=id).first()

        db.session.delete(appointment)
        db.session.commit()

        response_dict = {
            "delete_successful": True,
            "message": "Appointment deleted."    
        }

        response = make_response(jsonify(response_dict), 201)
        return response
    
class FeedbackResource(Resource):
    def get(self):
        feedbacks = [feedback.to_dict() for feedback in Feedback.query.all()]
        
        response= make_response( jsonify(feedbacks), 200)

        return response
    

    def post(self):
        new_feedback = Feedback(
            full_name=request.get_json()['full_name'],
            email=request.get_json()['email'],
            phonenumber= request.get_json()['phonenumber'],
            message=request.get_json()['message'],
            vehicle_make=request.get_json()['vehicle_make'],
            vehicle_no=request.get_json()['vehicle_no'],
            service=request.get_json()['service'], 
        )

        db.session.add(new_feedback)
        db.session.commit()

        feedback_dict = new_feedback.to_dict()

        response = make_response(jsonify(feedback_dict), 201)

        return response
    

class FeedbackById(Resource):
    def get(self,id):        
        feedback = Feedback.query.filter_by(id=id).first().to_dict()

        response = make_response(jsonify(feedback), 201)
        response.headers["Content-Type"]= "application/json"

        return response
        
    def patch(self,id):
        feedback = Feedback.query.filter_by(id=id).first()

        for attr in request.get_json():
            setattr(feedback, attr, request.get_json()[attr])

        db.session.add(feedback)
        db.session.commit()

        appointment_dict = feedback.to_dict()

        response = make_response(jsonify(appointment_dict), 201)

        return response

    def delete(self,id):     
        feedback = Feedback.query.filter_by(id=id).first()

        db.session.delete(feedback)
        db.session.commit()

        response_dict = {
            "delete_successful": True,
            "message": "Feedback deleted."    
        }

        response = make_response(jsonify(response_dict), 201)
        return response
    
    
    
    

api.add_resource(ProductResource, '/products')
api.add_resource(ProductById, '/product_id/<int:id>')
api.add_resource(AppointmentResource, '/appointments')
api.add_resource(AppointmentById, '/appointment_id/<int:id>')
api.add_resource(FeedbackResource, '/feedbacks')
api.add_resource(FeedbackById, '/feedback_id/<int:id>')


if __name__ =='__main__':
    app.run(debug=True, port=5000)