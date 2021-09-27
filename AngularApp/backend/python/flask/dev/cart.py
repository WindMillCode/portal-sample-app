from __main__ import app,db,ma,request,pprint,json,my_util,users,sqlalchemy
from users import User
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text
import uuid
from my_util import GUID

SQLALCHEMY_ECHO = True

class Cart(db.Model):
    cartId = db.Column(GUID(), primary_key=True, default=lambda: str(uuid.uuid4()))
    cart = db.Column(db.String, nullable = False)
    total = db.Column(db.Float, nullable = False)

    def __init__(self, cart, total):
        self.cart = cart
        self.total = total

    def any(self):
        return '<cart cartId = {} ,quantity ={},>'.format(self.cartId, self.quantity)

class CartSchema(ma.Schema):
    class Meta:
        fields = ('cartId','cart','total')

cart_schema = CartSchema()
carts_schema = CartSchema(many=True)


@app.route('/cart/create',methods=['PUT'])
def create_cart():
    cartData = request.json['cartData']
    userData = request.json['userData']
    if(userData['user'] != None):

        newCart= Cart(
            cart =  json.dumps(cartData['cart']),
            total = cartData['total']
        )
        cartId = newCart.cartId
        update_user_class = User.query.filter_by(user=userData['user']).first()
        if update_user_class is None:
            return {
                'message':{'message':'User not found'},
                'status':404
            }

        update_user_class.cartId = cartId

        db.session.add(newCart)
        db.session.flush()
        db.session.commit()
        return {
            'status':200,
            'message':{
                'message':'Cart created successfully',
                'cartId':cartId
            }
        }

@app.route('/cart/read',methods=['POST'])
def read_cart():
    
    None


@app.route('/cart/update',methods=['PATCH'])
def update_cart():
    None

@app.route('/cart/delete',methods=['DELETE'])
def delete_cart():
    None

@app.route('/cart/list',methods=['POST'])
def list_carts():
    carts = Cart.query.all()

    carts = [{
        'cartId':x.cartId,
        'cart':json.loads(x.cart),
        'total':x.total
    } for x in carts]
    return carts_schema.jsonify(carts)
    return {
        'status':200,
        'message':{
            'lists':carts_schema.jsonify(carts)
        }
    }

