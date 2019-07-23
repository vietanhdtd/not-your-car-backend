from flask import Flask, redirect, url_for, flash, render_template, jsonify, request
from flask_login import login_required, logout_user, current_user
from .config import Config
from .models import db, login_manager, Token, Car, Booking
from .oauth import blueprint
from .cli import create_db, add_products, delete
from flask_migrate import Migrate
from flask_cors import CORS
from datetime import datetime
from sqlalchemy import or_

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
app.register_blueprint(blueprint, url_prefix="/login")
db.init_app(app)
app.cli.add_command(add_products)
app.cli.add_command(delete)
login_manager.init_app(app)
migrate = Migrate(app, db, compare_type = True)

@app.route("/logout", methods = ['GET', 'POST'])
@login_required
def logout():
    token = Token.query.filter_by(user_id = current_user.id).first() 
    db.session.delete(token)
    db.session.commit()
    logout_user()
    return jsonify({
        "success": True
    })

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/user_profile", methods = ['post', 'get'])
@login_required
def user_profile():
    return jsonify({
        "success": True, 
        "user_id": current_user.id, 
        "user_name": current_user.name,
        "email": current_user.email
    })


@app.route("/cars", methods = ['post', 'get'])
def get_cars():
    data = Car.query.all()
    list_cars = []
    for car in data:
        cars = {
            'id':car.id,
            'owner_id': car.owner_id,
            'brand_name': car.brand_name,
            'model': car.model,
            'class_name': car.class_name,
            'gear_box': car.gear_box,
            'door': car.door,
            'price': car.price,
            'img': car.img,
            'description': car.description
        }
        list_cars.append(cars)
    return jsonify(list_cars)


@app.route('/create_post', methods = ['POST'])
@login_required
def create_post():
    data = request.get_json()
    total = Car.query.all()
    if data is None:
        data = {}
    if request.method == "POST":
        car = Car(brand_name = data.get('brand'),
                model = data.get('model'),
                class_name = data.get('class'),
                gear_box = data.get('gearbox'),
                door = data.get('door'),
                price = data.get('price'),
                img = data.get('img'),
                fuel = data.get('fuel'),
                status = "Available",
                description = data.get('description'))
        db.session.add(car)
        db.session.commit()
        return jsonify({
                    "success": True,
                    "total_car": len(total)
        })

@app.route('/booking', methods = ['POST', 'GET'])
@login_required
def booking():
    data = request.get_json()
    booking = Booking(location = data.get('location'),
                    pick_date = data.get('pick_date'),
                    return_date = data.get('return_date'),
                    car_id = data.get('car_id'))
    db.session.add(booking)
    db.session.commit()
    return jsonify({
                "success": True
    })

@app.route('/check', methods = ['POST', 'GET'])
def check():
    data = request.get_json()
    query_pick_date = datetime.strptime(data.get('pick_date'), '%Y-%m-%dT%H:%M:%S.%fZ')
    query_return_date = datetime.strptime(data.get('return_date'), '%Y-%m-%dT%H:%M:%S.%fZ')
    query_list = Booking.query.filter(or_(Booking.return_date <=  query_pick_date, Booking.pick_date >= query_return_date)).all()
    car_query = [Car.query.filter_by(id = query.car_id).one() for query in query_list]
    list_cars = []
    for car in car_query:
        cars = {
            'id':car.id,
            'owner_id': car.owner_id,
            'brand_name': car.brand_name,
            'model': car.model,
            'class_name': car.class_name,
            'gear_box': car.gear_box,
            'door': car.door,
            'price': car.price,
            'img': car.img,
            'description': car.description
        }
        list_cars.append(cars)
    return jsonify(list_cars)  
    