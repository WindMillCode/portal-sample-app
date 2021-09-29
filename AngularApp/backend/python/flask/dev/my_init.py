from __main__ import app,db,ma,request,pprint,json,my_util,users,sqlalchemy,requests,time
from products import Product


# if the products arent in the database add them
def init_products():
    products = Product.query.all()
    if len(products) == 0:
        [
            db.session.add(Product(
                ["QR Code 1","QR Code 2","NFT 1", "NFT 2","T-shirt 1","T shirt 2","T -shirt 3"][i],
                [
                    "./assets/media/shop_1.png",
                    "./assets/media/shop_1.png",
                    "./assets/media/shop_0.jpg",
                    "./assets/media/shop_0.jpg",
                    "./assets/media/shop_2.jpg",
                    "./assets/media/shop_3.jpg",
                    "./assets/media/shop_4.jpg"
                ][i],
                [29.99,29.99,54.99,54.99,22.99,25.99,22.99][i],
                1,
                "Simple Merch"
            )) for i,x in enumerate(range(0,7))
        ]
        db.session.commit()
    # pprint.pprint(products)
#



