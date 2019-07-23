import click
from flask.cli import with_appcontext
from .models import db, Car, User, Token, OAuth, Booking
import random


@click.command(name="createdb")
@with_appcontext
def create_db():
    db.create_all()
    db.session.commit()
    print("Database tables created")

@click.command(name="delete")
@with_appcontext
def delete():
    data = Booking.query.delete()
    db.session.commit()
    print(" tables clear")

@click.command(name="addproducts")
@with_appcontext
def add_products():
    for i in range(5):
        new_products = Car(owner_id = 2,
                                brand_name=f'Brand Name {i}',
                                model=f'model {i}',
                                class_name = 'SEDAN',
                                gear_box = "Auto",
                                door = 5,
                                price=random.randint(100, 10000)/100,
                                img='http://loremflickr.com/320/320/car',
                                description=f'Sample description for product{i}')
        db.session.add(new_products)
        db.session.commit()
        print("YES")    