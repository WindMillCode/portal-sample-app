from __main__ import app,db,ma,request,pprint,json,my_util,users,sqlalchemy
from users import User
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text
import uuid
from my_util import GUID

class Product(db.Model):
    productId = db.Column(GUID(), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(200), nullable = False)
    img_url = db.Column(db.String(1000))
    price = db.Column(db.Float, nullable = False)
    quantity = db.Column(db.Integer, nullable = False)

    desc = db.Column(db.String(3000), nullable = True)
   

    def __init__(self,title,img_url,price,quantity,desc):
        self.title = title
        self.img_url = img_url
        self.price = price
        self.quantity = quantity
        self.desc = desc
       

    def  any(self):
        return '<pro'

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('title','img_url','price','quantity','desc')

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@app.route('/product/create',methods=['PUT'])
def create_product():
    data = request.json['data']
    newproduct = Product(
        data['title'],
        data['img_url'],
        data['price'],
        data['quantity'],
        data['desc'],
       
    )

    db.session.add(newproduct)
    db.session.commit()
    return {
        'message':{'message':'CREATED'},

    },201

@app.route('/product/read',methods=['POST'])
def read_product():
    data = request.json['data']
    productID = data['title']
    product = Product.query.filter_by(title= productID).first()
    if product is None:
       return  {
           'message':{'message':'Product not found'},

        }, 404

    else:
       return  {
            'message':{
                'message':'OK',
                'data':product_schema.dump(product)
            },

        },200




@app.route('/product/update',methods=['PATCH'])
def update_product():
    data = request.json['data']
    product = data['title']
#update_body = data['update_body']
    update_product_class = Product.query.filter_by(title=product).first()
    pprint.pprint(update_product_class)
    if update_product_class is None:
        return {
            'message':{'message':'Product not found'},
        },404
    product_to_update = product_schema.dump(update_product_class)
    product_to_update.title= product_to_update["title"]
    product_to_update.img_url =product_to_update["img_url"]
    product_to_update.price = product_to_update["price"]
    product_to_update.desc = product_to_update["desc"]
    product_to_update.quantity = product_to_update["quantity"]
    

    db.session.flush()
    db.session.commit()
    return {
        'message':{
            'target':product_to_update
        },

    },200


@app.route('/product/delete',methods=['DELETE'])
def delete_product():
    data = request.json['data']
    product = Product.query.filter_by(title=data['title']).first()
    db.session.delete(product)
    db.session.commit()
    return {
        'message':{'message':'DELETED'},
    },200

    None

@app.route('/product/list',methods=['POST'])
def list_products():
    products = Product.query.all()
    products= [ {
        'title': x.title,
        'img_url': x.img_url,
        'price': x.price,
        'quantity':x.quantity,
        'desc': x.desc,
    } for x in products]
    return products_schema.jsonify(products), 200

