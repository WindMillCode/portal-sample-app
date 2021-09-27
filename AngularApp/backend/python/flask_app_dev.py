import sys
if sys.platform == "win32":
    sys.path.append(sys.path[0] + "\\site-packages\\windows")
elif sys.platform =="linux":
    sys.path.append(sys.path[0] + "/site-packages/linux")
from flask import Flask, request, redirect
from pyngrok import ngrok

# dev additions
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import pprint
import json
import my_util
#

app = Flask(__name__)
app.config.update(
    # SERVER_NAME="127.0.0.1:3005",
    USE_NGROK=True
)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
ma = Marshmallow(app)


class Products(db.Model):
    itemId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable = False)
    text = db.Column(db.String(3000), nullable = False)
    img_url = db.Column(db.String(1000))
    img_data = db.Column(db.LargeBinary) # I rather just use a storage service and place the url here
    price = db.Column(db.Float, nullable = False)

    def any(self):
        return '<product itemId = {} ,title ={}, text={}, price={},>'.format(self.itemId, self.title, self.price)

class Cart(db.Model):
    itemId = db.Column(db.Integer, primary_key=True)
    item_price = db.Column(db.Float, nullable = False)
    quantity = db.Column(db.Integer, nullable = False)

    def any(self):
        return '<cart itemId = {} ,quantity ={},>'.format(self.itemId, self.quantity)

class User(db.Model):
    user = db.Column(db.String(200), primary_key=True)
    myPass = db.Column(db.String(200),unique=True, nullable=False)
    billing = db.Column(db.String(20000))
    shipping = db.Column(db.String(2000))
    shipping_same_as_billing = db.Column(db.Boolean)

    def __init__ (self, user, myPass, billing, shipping, shipping_same_as_billing):
        self.user = user
        self.myPass = myPass
        self.billing = billing
        self.shipping = shipping
        self.shipping_same_as_billing = shipping_same_as_billing

    def any(self):
        return '<user user = {} ,myPass ={}, billing={}, shipping={}, shipping_same_as_billing={},>'.format(self.user, self.myPass, self.billing, self.shipping, self.shipping_same_as_billing)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('user', 'myPass','billing', 'shipping', 'shipping_same_as_billing')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

db.create_all()


@app.route('/users/update',methods=['PATCH'])
def update_user():
    # needs authentication before update
    data = request.json["data"]
    user = data['user']
    update_body = data['update_body']
    update_user_class = User.query.filter_by(user=user).first()
    pprint.pprint(update_user_class)
    if update_user_class is None:
        return {
            'message':{'message':'User not found'},
            'status':404
        }
    user_to_update = user_schema.dump(update_user_class)
    user_to_update["billing"] =  json.loads(user_to_update["billing"])
    user_to_update["shipping"] = json.loads(user_to_update["shipping"])
    user_to_update =  my_util.update_target(user_to_update,update_body)
    # user_to_update = my_util.update_dict(user_to_update,update_body)

    update_user_class.user = user_to_update["user"]
    update_user_class.myPass = user_to_update["myPass"]
    update_user_class.billing = json.dumps(user_to_update["billing"])
    update_user_class.shipping = json.dumps(user_to_update["shipping"])
    update_user_class.shipping_same_as_billing = user_to_update["shipping_same_as_billing"]

    db.session.flush()
    db.session.commit()
    return {
        'message':{
            'target':user_to_update
        },
        'status':200
    }



@app.route('/users/create',methods=['PUT'])
def create_user():
    pprint.pprint(request.json)
    data = request.json['data']
    newUser = User(
        data['user'],
        data['pass'],
        json.dumps(data['billing']),
        json.dumps(data['shipping']),
        data['shipping']['sameAsBilling']['checked']
    )
    db.session.add(newUser)
    db.session.commit()
    return {
        'message':{'message':'CREATED'},
        'status':201
    }


@app.route('/users/delete',methods=['DELETE'])
def delete_user():
    pprint.pprint(request.json)
    data = request.json['data']
    user = User.query.filter_by(user=data['user']).first()
    db.session.delete(user)
    db.session.commit()
    return {
        'message':{'message':'DELETED'},
        'status':200
    }

@app.route('/users/read',methods=['POST'])
def read_user():
    data = request.json['data']
    user =   data['user']
    mYpass = data['pass']
    user = User.query.filter_by(user=user).first()
    if user is None:
        return {
            'message':{'message':'User not found'},
            'status':404
        }
    elif user.myPass == mYpass:
        user.billing = json.loads(user.billing)
        user.shipping = json.loads(user.shipping)
        return {
            'message':{
                'message':'OK',
                'data':user_schema.dump(user)
            },
            'status':200,
        }

@app.route('/users/list',methods=['POST'])
def list_users():
    # if admin requests then supply, you dont want this on the backend

    users = User.query.all()
    users = [ {
        'user':x.user,
        'myPass':x.myPass,
        'billing':json.loads(x.billing),
        'shipping':json.loads(x.shipping),
    } for x in users]
    return users_schema.jsonify(users)


@app.route('/products/list', methods=['GET'])
def get_products():
	prod = Products.query.first()
	return prod.products



@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response



if __name__ == "__main__":
    port = 5000
    public_url = ngrok.connect(port).public_url
    print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))
    app.config["BASE_URL"] = public_url
    app.run(debug=True)
