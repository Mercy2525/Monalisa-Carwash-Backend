from models import Appointment,Product,Feedback,db
from faker import Faker
import random
from random import choice as rc

from app import app
fake=Faker()

with app.app_context():
    Product.query.delete()
    Appointment.query.delete()
    Feedback.query.delete()

    products=[]

    for i in range(4):
        product=Product(product_name=fake.text(15), cost=random.randint(200,1000), image=fake.url())

        products.append(product)
        db.session.add_all(products)
        db.session.commit()

    appointments= []

    for i in range(4):
        appointment=Appointment(full_name=fake.name(),email=fake.email(), phonenumber=fake.phone_number(), message=fake.sentence(), service=fake.sentence(), vehicle_make=fake.sentence(),time_frame=rc(['morning','afternoon']),vehicle_model=random.randint(300,5000))

        appointments.append(appointment)
        db.session.add_all(appointments)
        db.session.commit()

    feedbacks= []

    for i in range(4):
        feedback=Feedback(full_name=fake.name(),email=fake.email(), phonenumber=fake.phone_number(), message=fake.sentence(), vehicle_make=fake.sentence(), service=fake.sentence(), vehicle_no=random.randint(300,5000))

        feedbacks.append(feedback)
        db.session.add_all(feedbacks)
        db.session.commit()

    print('done seeding...')



