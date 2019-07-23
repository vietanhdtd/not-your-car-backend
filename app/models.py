from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    
    post = db.relationship('Car', backref = 'owner', lazy = True )
    
class OAuth(OAuthConsumerMixin, db.Model):
    provider_user_id = db.Column(db.String(256), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    user = db.relationship(User)

class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    user = db.relationship(User)
    
class Car (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    brand_name = db.Column(db.String(255), nullable = False)
    model = db.Column(db.String(255), nullable = False)
    class_name = db.Column(db.String(255), nullable = False)
    gear_box = db.Column(db.String(255), nullable = False)
    door = db.Column(db.String(255), nullable = False)
    img = db.Column(db.String(255), nullable = False)
    fuel = db.Column(db.String(255), nullable = False)
    description = db.Column(db.String(999), nullable = False)
    price = db.Column(db.String(255), nullable = False)
    status = db.Column(db.String(255), nullable = False)
    date_create = db.Column(db.DateTime, server_default = db.func.now())

    rent_user = db.relationship('Booking', backref = 'Rental', lazy = True)

    


class Booking (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'))
    location = db.Column(db.String(255), nullable = False)
    pick_date = db.Column(db.DateTime(), nullable = False)
    return_date = db.Column(db.DateTime(), nullable = False)
    

class Billing (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    total_bill = db.Column(db.String(255), nullable = False)
    date_create = db.Column(db.String(255), nullable = False)


# setup login manager
login_manager = LoginManager()
# login_manager.login_view = "facebook.login"


@login_manager.request_loader
def load_user_from_request(request):
    # Login Using our Custom Header
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Token ', '', 1)
        token = Token.query.filter_by(uuid=api_key).first()
        if token:
            return token.user
    return None
