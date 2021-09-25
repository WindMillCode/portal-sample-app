import sys
if sys.platform == "win32":
    sys.path.append(sys.path[0] + "\\site-packages\\windows")
elif sys.platform =="linux":
    sys.path.append(sys.path[0] + "/site-packages/linux")
from flask import Flask, request, redirect
from pyngrok import ngrok

# dev additions
from flask_sqlalchemy import SQLAlchemy
#

app = Flask(__name__)
app.config.update(
    # SERVER_NAME="127.0.0.1:3005",
    USE_NGROK=True
)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db=SQLAlchemy(app)


class Products(db.Model):
    itemId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable = False)
    text = db.Column(db.String(3000), nullable = False)
    img = db.Column(db.String())
    img_data = db.Column(db.LargeBinary)
    price = db.Column(db.Integer, nullable = False)

    def any(self):
        return '<product itemId = {} ,title ={}, text={}, price={},>'.format(self.itemId, self.title, self.price)


#function to list products
@app.route('/products', methods=['GET'])
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
