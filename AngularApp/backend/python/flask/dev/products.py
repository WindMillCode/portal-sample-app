from __main__ import app,db,ma,request,pprint,json,my_util

class Products(db.Model):
    itemId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable = False)
    text = db.Column(db.String(3000), nullable = False)
    img_url = db.Column(db.String(1000))
    img_data = db.Column(db.LargeBinary) # I rather just use a storage service and place the url here
    price = db.Column(db.Float, nullable = False)

    def any(self):
        return '<product itemId = {} ,title ={}, text={}, price={},>'.format(self.itemId, self.title, self.price)

@app.route('/products/list', methods=['GET'])
def get_products():
	prod = Products.query.first()
	return prod.products
