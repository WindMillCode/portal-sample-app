from __main__ import app,db,ma,request,pprint,json,my_util,users,sqlalchemy,requests,time
from products import Product
from orders import Order
from users import User


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


# init some orders
def init_orders():
    in_db = Order.query.all()
    if len(in_db) == 0:
        my_sample = [
            {
                "billing": {
                "items": {
                    "address": "562 Guiseppe Summit",
                    "city": "Chaimview",
                    "country": "Colombia",
                    "email": "Isabelle.Fritsch@yahoo.com",
                    "first_name": "Vesta",
                    "last_name": "Witting",
                    "phone": "892-732-0528 x4655",
                    "state": "Michigan",
                    "zip_code": "75617-3847"
                }
                },
                "cart": [
                {
                    "name": "T shirt 2",
                    "price": 25.99,
                    "quantity": 2
                },
                {
                    "name": "NFT 1",
                    "price": 54.99,
                    "quantity": 2
                }
                ],
                "orderId": "ffbebaad-ac7f-441f-ad05-16d65879efbe",
                "shipping": {
                "info": {
                    "items": {
                    "address": "562 Guiseppe Summit",
                    "city": "Chaimview",
                    "country": "Colombia",
                    "email": "Isabelle.Fritsch@yahoo.com",
                    "first_name": "Vesta",
                    "last_name": "Witting",
                    "phone": "892-732-0528 x4655",
                    "state": "Michigan",
                    "zip_code": "75617-3847"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 2112.34,
                "user": "Joma34543"
            },
            {
                "billing": {
                "items": {
                    "address": "3368 Prosacco Glens",
                    "city": "North Dudley",
                    "country": "Saint Barthelemy",
                    "email": "Selmer70@gmail.com",
                    "first_name": "Eda",
                    "last_name": "Pacocha",
                    "phone": "(653) 829-0705",
                    "state": "Utah",
                    "zip_code": "71169"
                }
                },
                "cart": [
                {
                    "name": "T-shirt 1",
                    "price": 22.99,
                    "quantity": 1
                },
                {
                    "name": "QR Code 2",
                    "price": 29.99,
                    "quantity": 3
                }
                ],
                "orderId": "d55ed020-2385-4baf-a597-d3980e2e29d1",
                "shipping": {
                "info": {
                    "items": {
                    "address": "46462 Cielo Lakes",
                    "city": "Hillschester",
                    "country": "Haiti",
                    "email": "Geovany.Kulas72@hotmail.com",
                    "first_name": "Cathryn",
                    "last_name": "Roberts",
                    "phone": "422.344.8631 x10358",
                    "state": "Illinois",
                    "zip_code": "38070"
                    }
                },
                "sameAsBilling": {
                    "checked": False
                }
                },
                "total": 112.96,
                "user": "Nathanial_Pfeffer74"
            },
            {
                "billing": {
                "items": {
                    "address": "625 Gleason Tunnel",
                    "city": "South Ubaldoview",
                    "country": "Romania",
                    "email": "Shanna.Wuckert@hotmail.com",
                    "first_name": "Lyric",
                    "last_name": "Heller",
                    "phone": "269-543-2105 x978",
                    "state": "Arkansas",
                    "zip_code": "70005"
                }
                },
                "cart": [
                {
                    "name": "T-shirt 1",
                    "price": 22.99,
                    "quantity": 1
                },
                {
                    "name": "QR Code 2",
                    "price": 29.99,
                    "quantity": 3
                }
                ],
                "orderId": "7bb9aa2d-029f-4ba4-9a7b-8b5389788957",
                "shipping": {
                "info": {
                    "items": {
                    "address": "625 Gleason Tunnel",
                    "city": "South Ubaldoview",
                    "country": "Romania",
                    "email": "Shanna.Wuckert@hotmail.com",
                    "first_name": "Lyric",
                    "last_name": "Heller",
                    "phone": "269-543-2105 x978",
                    "state": "Arkansas",
                    "zip_code": "70005"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 112.96,
                "user": "Nathanial_Pfeffer74"
            },
            {
                "billing": {
                "items": {
                    "address": "1557 Beahan Harbors",
                    "city": "Davie",
                    "country": "Ghana",
                    "email": "Ed.Collier12@yahoo.com",
                    "first_name": "Carter",
                    "last_name": "Fritsch",
                    "phone": "230.938.5220 x358",
                    "state": "Tennessee",
                    "zip_code": "90262-1012"
                }
                },
                "cart": [
                {
                    "name": "NFT 2",
                    "price": 54.99,
                    "quantity": 5
                },
                {
                    "name": "QR Code 2",
                    "price": 29.99,
                    "quantity": 3
                }
                ],
                "orderId": "2131f074-d88f-4d74-9386-1a3fe50e12cd",
                "shipping": {
                "info": {
                    "items": {
                    "address": "1557 Beahan Harbors",
                    "city": "Davie",
                    "country": "Ghana",
                    "email": "Ed.Collier12@yahoo.com",
                    "first_name": "Carter",
                    "last_name": "Fritsch",
                    "phone": "230.938.5220 x358",
                    "state": "Tennessee",
                    "zip_code": "90262-1012"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 364.92,
                "user": "Allan_Murphy62"
            },
            {
                "billing": {
                "items": {
                    "address": "9343 Darian Passage",
                    "city": "Jerrodville",
                    "country": "Rwanda",
                    "email": "Osborne_Kessler99@gmail.com",
                    "first_name": "Ellie",
                    "last_name": "Feest",
                    "phone": "944.698.0950 x507",
                    "state": "Pennsylvania",
                    "zip_code": "71156"
                }
                },
                "cart": [
                {
                    "name": "QR Code 2",
                    "price": 29.99,
                    "quantity": 5
                },
                {
                    "name": "NFT 1",
                    "price": 54.99,
                    "quantity": 3
                }
                ],
                "orderId": "cbd865e2-616f-4922-890f-b30dceff3176",
                "shipping": {
                "info": {
                    "items": {
                    "address": "9343 Darian Passage",
                    "city": "Jerrodville",
                    "country": "Rwanda",
                    "email": "Osborne_Kessler99@gmail.com",
                    "first_name": "Ellie",
                    "last_name": "Feest",
                    "phone": "944.698.0950 x507",
                    "state": "Pennsylvania",
                    "zip_code": "71156"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 314.92,
                "user": "Michele74"
            },
            {
                "billing": {
                "items": {
                    "address": "27922 Johann Trace",
                    "city": "New Cameronside",
                    "country": "Monaco",
                    "email": "Audra_Powlowski@yahoo.com",
                    "first_name": "America",
                    "last_name": "Kassulke",
                    "phone": "299-820-7214 x373",
                    "state": "Georgia",
                    "zip_code": "34458-1952"
                }
                },
                "cart": [
                {
                    "name": "NFT 1",
                    "price": 54.99,
                    "quantity": 4
                },
                {
                    "name": "QR Code 2",
                    "price": 29.99,
                    "quantity": 5
                }
                ],
                "orderId": "fa404ea0-afb3-473a-a39f-7326f2a8d47a",
                "shipping": {
                "info": {
                    "items": {
                    "address": "27922 Johann Trace",
                    "city": "New Cameronside",
                    "country": "Monaco",
                    "email": "Audra_Powlowski@yahoo.com",
                    "first_name": "America",
                    "last_name": "Kassulke",
                    "phone": "299-820-7214 x373",
                    "state": "Georgia",
                    "zip_code": "34458-1952"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 369.91,
                "user": "Naomie4"
            },
            {
                "billing": {
                "items": {
                    "address": "6061 Kub Harbors",
                    "city": "Mohrton",
                    "country": "Svalbard & Jan Mayen Islands",
                    "email": "Eduardo60@yahoo.com",
                    "first_name": "Oral",
                    "last_name": "Bednar",
                    "phone": "(850) 683-3559",
                    "state": "Pennsylvania",
                    "zip_code": "79323"
                }
                },
                "cart": [
                {
                    "name": "T shirt 2",
                    "price": 25.99,
                    "quantity": 1
                },
                {
                    "name": "QR Code 1",
                    "price": 29.99,
                    "quantity": 1
                }
                ],
                "orderId": "f863e583-5ac0-4170-8434-d241839c791b",
                "shipping": {
                "info": {
                    "items": {
                    "address": "6061 Kub Harbors",
                    "city": "Mohrton",
                    "country": "Svalbard & Jan Mayen Islands",
                    "email": "Eduardo60@yahoo.com",
                    "first_name": "Oral",
                    "last_name": "Bednar",
                    "phone": "(850) 683-3559",
                    "state": "Pennsylvania",
                    "zip_code": "79323"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 55.98,
                "user": "Maxine66"
            },
            {
                "billing": {
                "items": {
                    "address": "7771 Grant Lake",
                    "city": "Port Ivy",
                    "country": "Belarus",
                    "email": "Tina47@gmail.com",
                    "first_name": "Lacy",
                    "last_name": "Turner",
                    "phone": "986.217.2334 x6046",
                    "state": "Pennsylvania",
                    "zip_code": "11969"
                }
                },
                "cart": [
                {
                    "name": "T shirt 2",
                    "price": 25.99,
                    "quantity": 1
                },
                {
                    "name": "NFT 1",
                    "price": 54.99,
                    "quantity": 5
                }
                ],
                "orderId": "9b3311ed-b67e-41c3-86ec-fa397e0e9395",
                "shipping": {
                "info": {
                    "items": {
                    "address": "7771 Grant Lake",
                    "city": "Port Ivy",
                    "country": "Belarus",
                    "email": "Tina47@gmail.com",
                    "first_name": "Lacy",
                    "last_name": "Turner",
                    "phone": "986.217.2334 x6046",
                    "state": "Pennsylvania",
                    "zip_code": "11969"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 300.94,
                "user": "Kamille98"
            },
            {
                "billing": {
                "items": {
                    "address": "53498 Blake Stream",
                    "city": "Lake Gregory",
                    "country": "Belgium",
                    "email": "Nadia_Gleason19@yahoo.com",
                    "first_name": "Tanya",
                    "last_name": "Runolfsson",
                    "phone": "1-504-260-5915",
                    "state": "Vermont",
                    "zip_code": "85474-7746"
                }
                },
                "cart": [
                {
                    "name": "NFT 2",
                    "price": 54.99,
                    "quantity": 4
                },
                {
                    "name": "NFT 1",
                    "price": 54.99,
                    "quantity": 3
                }
                ],
                "orderId": "4ee91f33-e599-45b7-8058-12ae63065050",
                "shipping": {
                "info": {
                    "items": {
                    "address": "53498 Blake Stream",
                    "city": "Lake Gregory",
                    "country": "Belgium",
                    "email": "Nadia_Gleason19@yahoo.com",
                    "first_name": "Tanya",
                    "last_name": "Runolfsson",
                    "phone": "1-504-260-5915",
                    "state": "Vermont",
                    "zip_code": "85474-7746"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 384.93,
                "user": "Kaitlyn53"
            },
            {
                "billing": {
                "items": {
                    "address": "7141 Kiera Meadow",
                    "city": "Skilesview",
                    "country": "Cameroon",
                    "email": "Hermina_Huel9@yahoo.com",
                    "first_name": "Bernadine",
                    "last_name": "Collins",
                    "phone": "482.502.9309 x27234",
                    "state": "Arkansas",
                    "zip_code": "20019"
                }
                },
                "cart": [
                {
                    "name": "NFT 1",
                    "price": 54.99,
                    "quantity": 4
                }
                ],
                "orderId": "3b34ee68-3465-4b1c-81ef-29339a5ff14b",
                "shipping": {
                "info": {
                    "items": {
                    "address": "7141 Kiera Meadow",
                    "city": "Skilesview",
                    "country": "Cameroon",
                    "email": "Hermina_Huel9@yahoo.com",
                    "first_name": "Bernadine",
                    "last_name": "Collins",
                    "phone": "482.502.9309 x27234",
                    "state": "Arkansas",
                    "zip_code": "20019"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 219.96,
                "user": "Johnathon_Jerde12"
            },
            {
                "billing": {
                "items": {
                    "address": "1275 Edwina Causeway",
                    "city": "New Aaron",
                    "country": "French Guiana",
                    "email": "Rickie_Reynolds@yahoo.com",
                    "first_name": "Annalise",
                    "last_name": "Mante",
                    "phone": "740.402.8741 x31068",
                    "state": "Mississippi",
                    "zip_code": "73147-5384"
                }
                },
                "cart": [
                {
                    "name": "T-shirt 1",
                    "price": 22.99,
                    "quantity": 3
                },
                {
                    "name": "NFT 1",
                    "price": 54.99,
                    "quantity": 5
                }
                ],
                "orderId": "ad99adf7-7fb2-4d41-9e24-af212a0dc9e0",
                "shipping": {
                "info": {
                    "items": {
                    "address": "1275 Edwina Causeway",
                    "city": "New Aaron",
                    "country": "French Guiana",
                    "email": "Rickie_Reynolds@yahoo.com",
                    "first_name": "Annalise",
                    "last_name": "Mante",
                    "phone": "740.402.8741 x31068",
                    "state": "Mississippi",
                    "zip_code": "73147-5384"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 343.92,
                "user": "Demetris.Fadel"
            },
            {
                "billing": {
                "items": {
                    "address": "94549 Streich Common",
                    "city": "Lorainebury",
                    "country": "Samoa",
                    "email": "Rosalind44@yahoo.com",
                    "first_name": "Jay",
                    "last_name": "Lindgren",
                    "phone": "253-409-6932 x971",
                    "state": "Florida",
                    "zip_code": "97418"
                }
                },
                "cart": [
                {
                    "name": "T shirt 2",
                    "price": 25.99,
                    "quantity": 1
                },
                {
                    "name": "NFT 2",
                    "price": 54.99,
                    "quantity": 1
                }
                ],
                "orderId": "72b18898-1c19-4598-95b0-3fba703d8737",
                "shipping": {
                "info": {
                    "items": {
                    "address": "7931 Lang Centers",
                    "city": "South Tierraville",
                    "country": "Senegal",
                    "email": "Leif47@yahoo.com",
                    "first_name": "Susie",
                    "last_name": "Fisher",
                    "phone": "1-223-318-2779 x994",
                    "state": "West Virginia",
                    "zip_code": "66422-6290"
                    }
                },
                "sameAsBilling": {
                    "checked": False
                }
                },
                "total": 80.98,
                "user": "Bailey92"
            },
            {
                "billing": {
                "items": {
                    "address": "665 Bailey Falls",
                    "city": "Shanamouth",
                    "country": "Jersey",
                    "email": "Gladyce_Renner95@gmail.com",
                    "first_name": "Roy",
                    "last_name": "Schneider",
                    "phone": "(222) 504-1630",
                    "state": "New Mexico",
                    "zip_code": "77595"
                }
                },
                "cart": [
                {
                    "name": "NFT 2",
                    "price": 54.99,
                    "quantity": 1
                },
                {
                    "name": "QR Code 2",
                    "price": 29.99,
                    "quantity": 5
                }
                ],
                "orderId": "6dd5c8d7-c0fe-4e32-ad7f-cf10633f621d",
                "shipping": {
                "info": {
                    "items": {
                    "address": "665 Bailey Falls",
                    "city": "Shanamouth",
                    "country": "Jersey",
                    "email": "Gladyce_Renner95@gmail.com",
                    "first_name": "Roy",
                    "last_name": "Schneider",
                    "phone": "(222) 504-1630",
                    "state": "New Mexico",
                    "zip_code": "77595"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 204.94,
                "user": "Kacey.Kuphal60"
            },
            {
                "billing": {
                "items": {
                    "address": "43672 Alec Mountains",
                    "city": "North Lilla",
                    "country": "Morocco",
                    "email": "Kaylie57@yahoo.com",
                    "first_name": "Helene",
                    "last_name": "Barton",
                    "phone": "1-443-368-3012",
                    "state": "Idaho",
                    "zip_code": "05950-8788"
                }
                },
                "cart": [
                {
                    "name": "T shirt 2",
                    "price": 25.99,
                    "quantity": 3
                },
                {
                    "name": "QR Code 2",
                    "price": 29.99,
                    "quantity": 3
                }
                ],
                "orderId": "d150960d-4ee7-4e8a-b556-37184bd01df5",
                "shipping": {
                "info": {
                    "items": {
                    "address": "7024 Marley Underpass",
                    "city": "Vinnieside",
                    "country": "Norfolk Island",
                    "email": "Kavon19@gmail.com",
                    "first_name": "Jorge",
                    "last_name": "Smith",
                    "phone": "(581) 866-5629",
                    "state": "Vermont",
                    "zip_code": "23205"
                    }
                },
                "sameAsBilling": {
                    "checked": False
                }
                },
                "total": 167.94,
                "user": "Emile83"
            },
            {
                "billing": {
                "items": {
                    "address": "8446 Spencer Courts",
                    "city": "East Rodrickmouth",
                    "country": "Cyprus",
                    "email": "Alden50@hotmail.com",
                    "first_name": "Sister",
                    "last_name": "Koelpin",
                    "phone": "718.835.6783 x2234",
                    "state": "Louisiana",
                    "zip_code": "14346"
                }
                },
                "cart": [
                {
                    "name": "QR Code 2",
                    "price": 29.99,
                    "quantity": 3
                },
                {
                    "name": "T-shirt 1",
                    "price": 22.99,
                    "quantity": 4
                }
                ],
                "orderId": "396048ba-06af-47b0-9325-2295ed9a8ed7",
                "shipping": {
                "info": {
                    "items": {
                    "address": "694 Gorczany Manors",
                    "city": "North Keon",
                    "country": "Anguilla",
                    "email": "Aubree_Nitzsche70@yahoo.com",
                    "first_name": "Zita",
                    "last_name": "Fisher",
                    "phone": "390-415-5125",
                    "state": "Massachusetts",
                    "zip_code": "88880"
                    }
                },
                "sameAsBilling": {
                    "checked": False
                }
                },
                "total": 181.93,
                "user": "Kathryne_Blanda3"
            },
            {
                "billing": {
                "items": {
                    "address": "50740 Brent Isle",
                    "city": "Florianton",
                    "country": "Cape Verde",
                    "email": "Lorine.Abernathy96@gmail.com",
                    "first_name": "Lula",
                    "last_name": "Wolff",
                    "phone": "731-869-3932",
                    "state": "New Jersey",
                    "zip_code": "96019"
                }
                },
                "cart": [
                {
                    "name": "T shirt 2",
                    "price": 25.99,
                    "quantity": 5
                },
                {
                    "name": "T-shirt 1",
                    "price": 22.99,
                    "quantity": 3
                }
                ],
                "orderId": "bf9f9e7e-6501-44e7-82f2-047da1ee70d4",
                "shipping": {
                "info": {
                    "items": {
                    "address": "936 Baron Pine",
                    "city": "North Donaldmouth",
                    "country": "Kazakhstan",
                    "email": "Kali92@hotmail.com",
                    "first_name": "Chet",
                    "last_name": "O'Kon",
                    "phone": "(982) 317-4330 x145",
                    "state": "Nebraska",
                    "zip_code": "38346"
                    }
                },
                "sameAsBilling": {
                    "checked": False
                }
                },
                "total": 198.92,
                "user": "Felipe.Trantow"
            },
            {
                "billing": {
                "items": {
                    "address": "84485 Wisozk Viaduct",
                    "city": "Wolffbury",
                    "country": "Denmark",
                    "email": "Kaci.Maggio67@hotmail.com",
                    "first_name": "Elton",
                    "last_name": "Davis",
                    "phone": "1-810-512-0440 x26600",
                    "state": "Indiana",
                    "zip_code": "18856"
                }
                },
                "cart": [
                {
                    "name": "T shirt 2",
                    "price": 25.99,
                    "quantity": 5
                },
                {
                    "name": "T-shirt 1",
                    "price": 22.99,
                    "quantity": 3
                }
                ],
                "orderId": "609e425b-7e30-4443-b994-802ac2b0757e",
                "shipping": {
                "info": {
                    "items": {
                    "address": "84485 Wisozk Viaduct",
                    "city": "Wolffbury",
                    "country": "Denmark",
                    "email": "Kaci.Maggio67@hotmail.com",
                    "first_name": "Elton",
                    "last_name": "Davis",
                    "phone": "1-810-512-0440 x26600",
                    "state": "Indiana",
                    "zip_code": "18856"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 198.92,
                "user": "Felipe.Trantow"
            },
            {
                "billing": {
                "items": {
                    "address": "62130 Constantin Garden",
                    "city": "Oak Park",
                    "country": "Saint Helena",
                    "email": "Merl.Bartoletti@gmail.com",
                    "first_name": "Dorcas",
                    "last_name": "Beatty",
                    "phone": "(371) 950-5900 x337",
                    "state": "Utah",
                    "zip_code": "10587-0769"
                }
                },
                "cart": [
                {
                    "name": "NFT 2",
                    "price": 54.99,
                    "quantity": 1
                },
                {
                    "name": "QR Code 1",
                    "price": 29.99,
                    "quantity": 1
                }
                ],
                "orderId": "897eafa5-3592-44ba-b825-a0b26ad23dd5",
                "shipping": {
                "info": {
                    "items": {
                    "address": "62130 Constantin Garden",
                    "city": "Oak Park",
                    "country": "Saint Helena",
                    "email": "Merl.Bartoletti@gmail.com",
                    "first_name": "Dorcas",
                    "last_name": "Beatty",
                    "phone": "(371) 950-5900 x337",
                    "state": "Utah",
                    "zip_code": "10587-0769"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 84.98,
                "user": "Janice70"
            },
            {
                "billing": {
                "items": {
                    "address": "221 Maxine Estates",
                    "city": "Mitchelltown",
                    "country": "Mauritania",
                    "email": "Stevie63@gmail.com",
                    "first_name": "Travis",
                    "last_name": "Gaylord",
                    "phone": "1-242-369-0625",
                    "state": "Maryland",
                    "zip_code": "02424-5651"
                }
                },
                "cart": [
                {
                    "name": "NFT 2",
                    "price": 54.99,
                    "quantity": 1
                },
                {
                    "name": "QR Code 1",
                    "price": 29.99,
                    "quantity": 1
                }
                ],
                "orderId": "cbf32b27-756b-4ca0-8f57-c870d410860f",
                "shipping": {
                "info": {
                    "items": {
                    "address": "668 Zemlak Falls",
                    "city": "East Pansyville",
                    "country": "French Guiana",
                    "email": "Robert.Wolff34@hotmail.com",
                    "first_name": "Velma",
                    "last_name": "Medhurst",
                    "phone": "1-577-446-6223",
                    "state": "Arizona",
                    "zip_code": "41921"
                    }
                },
                "sameAsBilling": {
                    "checked": False
                }
                },
                "total": 84.98,
                "user": "Janice70"
            },
            {
                "billing": {
                "items": {
                    "address": "8006 Eulalia Greens",
                    "city": "West Trishamouth",
                    "country": "Burkina Faso",
                    "email": "Timmothy.Yost26@gmail.com",
                    "first_name": "Valerie",
                    "last_name": "Erdman",
                    "phone": "907.289.4805 x611",
                    "state": "Missouri",
                    "zip_code": "31705-7492"
                }
                },
                "cart": [
                {
                    "name": "NFT 2",
                    "price": 54.99,
                    "quantity": 5
                },
                {
                    "name": "T-shirt 1",
                    "price": 22.99,
                    "quantity": 1
                }
                ],
                "orderId": "00d3771d-aa58-4e19-8b46-df422adabf5d",
                "shipping": {
                "info": {
                    "items": {
                    "address": "8006 Eulalia Greens",
                    "city": "West Trishamouth",
                    "country": "Burkina Faso",
                    "email": "Timmothy.Yost26@gmail.com",
                    "first_name": "Valerie",
                    "last_name": "Erdman",
                    "phone": "907.289.4805 x611",
                    "state": "Missouri",
                    "zip_code": "31705-7492"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 297.94,
                "user": "Jamison.Funk"
            },
            {
                "billing": {
                "items": {
                    "address": "406 Germaine Landing",
                    "city": "Mullerfort",
                    "country": "Cook Islands",
                    "email": "Jeffry_McClure@yahoo.com",
                    "first_name": "Josue",
                    "last_name": "Reynolds",
                    "phone": "893-949-5420 x8877",
                    "state": "California",
                    "zip_code": "57370-2472"
                }
                },
                "cart": [
                {
                    "name": "NFT 1",
                    "price": 54.99,
                    "quantity": 5
                },
                {
                    "name": "QR Code 1",
                    "price": 29.99,
                    "quantity": 1
                }
                ],
                "orderId": "c1b3c6e4-0fba-499e-bc71-5c5975fc0dd9",
                "shipping": {
                "info": {
                    "items": {
                    "address": "1993 Jaydon Gardens",
                    "city": "Lake Brandomouth",
                    "country": "Brunei Darussalam",
                    "email": "Aliya91@hotmail.com",
                    "first_name": "Kurt",
                    "last_name": "Maggio",
                    "phone": "521-559-9581",
                    "state": "Nevada",
                    "zip_code": "83878-3055"
                    }
                },
                "sameAsBilling": {
                    "checked": False
                }
                },
                "total": 304.94,
                "user": "Alexandro78"
            },
            {
                "billing": {
                "items": {
                    "address": "90774 Marquardt Hills",
                    "city": "Wymanville",
                    "country": "Ghana",
                    "email": "Holly_Corwin1@gmail.com",
                    "first_name": "Retha",
                    "last_name": "Nikolaus",
                    "phone": "938-456-9627 x58051",
                    "state": "Wisconsin",
                    "zip_code": "33097"
                }
                },
                "cart": [
                {
                    "name": "NFT 2",
                    "price": 54.99,
                    "quantity": 2
                },
                {
                    "name": "T-shirt 1",
                    "price": 22.99,
                    "quantity": 1
                }
                ],
                "orderId": "9d4b3fa0-c26c-4685-9fa4-bed5ba8a8251",
                "shipping": {
                "info": {
                    "items": {
                    "address": "90774 Marquardt Hills",
                    "city": "Wymanville",
                    "country": "Ghana",
                    "email": "Holly_Corwin1@gmail.com",
                    "first_name": "Retha",
                    "last_name": "Nikolaus",
                    "phone": "938-456-9627 x58051",
                    "state": "Wisconsin",
                    "zip_code": "33097"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 132.97,
                "user": "Katheryn_Lynch45"
            },
            {
                "billing": {
                "items": {
                    "address": "2430 Hartmann Canyon",
                    "city": "Grimesview",
                    "country": "Malta",
                    "email": "Kelly16@gmail.com",
                    "first_name": "Casandra",
                    "last_name": "Haag",
                    "phone": "1-997-537-3038 x43728",
                    "state": "Indiana",
                    "zip_code": "03466"
                }
                },
                "cart": [
                {
                    "name": "QR Code 2",
                    "price": 29.99,
                    "quantity": 5
                },
                {
                    "name": "QR Code 1",
                    "price": 29.99,
                    "quantity": 1
                }
                ],
                "orderId": "d392c35f-962f-4043-9620-8a20872f963b",
                "shipping": {
                "info": {
                    "items": {
                    "address": "2430 Hartmann Canyon",
                    "city": "Grimesview",
                    "country": "Malta",
                    "email": "Kelly16@gmail.com",
                    "first_name": "Casandra",
                    "last_name": "Haag",
                    "phone": "1-997-537-3038 x43728",
                    "state": "Indiana",
                    "zip_code": "03466"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 179.94,
                "user": "Mariam44"
            },
            {
                "billing": {
                "items": {
                    "address": "27570 Heathcote Cape",
                    "city": "Dareside",
                    "country": "Christmas Island",
                    "email": "Anna_Gottlieb50@yahoo.com",
                    "first_name": "Keira",
                    "last_name": "Gulgowski",
                    "phone": "1-534-825-3065 x31161",
                    "state": "Massachusetts",
                    "zip_code": "45305-3054"
                }
                },
                "cart": [
                {
                    "name": "NFT 1",
                    "price": 54.99,
                    "quantity": 4
                },
                {
                    "name": "QR Code 2",
                    "price": 29.99,
                    "quantity": 1
                }
                ],
                "orderId": "9f3a5786-091f-4ff0-bc0f-73f11ad493fb",
                "shipping": {
                "info": {
                    "items": {
                    "address": "27570 Heathcote Cape",
                    "city": "Dareside",
                    "country": "Christmas Island",
                    "email": "Anna_Gottlieb50@yahoo.com",
                    "first_name": "Keira",
                    "last_name": "Gulgowski",
                    "phone": "1-534-825-3065 x31161",
                    "state": "Massachusetts",
                    "zip_code": "45305-3054"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 249.95,
                "user": "Loma.Leffler"
            },
            {
                "billing": {
                "items": {
                    "address": "2294 Johnson Port",
                    "city": "Port Elwyn",
                    "country": "United States Minor Outlying Islands",
                    "email": "Donnell75@gmail.com",
                    "first_name": "Dino",
                    "last_name": "Mertz",
                    "phone": "964-497-5897 x07175",
                    "state": "Oregon",
                    "zip_code": "86460"
                }
                },
                "cart": [
                {
                    "name": "NFT 1",
                    "price": 54.99,
                    "quantity": 4
                },
                {
                    "name": "QR Code 2",
                    "price": 29.99,
                    "quantity": 1
                }
                ],
                "orderId": "e94e07ac-bf73-4164-aae8-4a7b37bf3ccf",
                "shipping": {
                "info": {
                    "items": {
                    "address": "322 Turner Turnpike",
                    "city": "Uptonchester",
                    "country": "Gambia",
                    "email": "Ervin_Towne@yahoo.com",
                    "first_name": "Jannie",
                    "last_name": "Kuhn",
                    "phone": "(755) 710-8479 x7915",
                    "state": "Colorado",
                    "zip_code": "41910"
                    }
                },
                "sameAsBilling": {
                    "checked": False
                }
                },
                "total": 249.95,
                "user": "Loma.Leffler"
            },
            {
                "billing": {
                "items": {
                    "address": "54033 Weissnat Fork",
                    "city": "East Luisa",
                    "country": "Virgin Islands, U.S.",
                    "email": "Jairo_Moen@gmail.com",
                    "first_name": "Tevin",
                    "last_name": "Abbott",
                    "phone": "980.310.3714 x082",
                    "state": "Delaware",
                    "zip_code": "91034"
                }
                },
                "cart": [
                {
                    "name": "T-shirt 1",
                    "price": 22.99,
                    "quantity": 2
                },
                {
                    "name": "QR Code 1",
                    "price": 29.99,
                    "quantity": 1
                }
                ],
                "orderId": "d9efa69a-3f7f-4496-81c7-407b0a1c37bd",
                "shipping": {
                "info": {
                    "items": {
                    "address": "54033 Weissnat Fork",
                    "city": "East Luisa",
                    "country": "Virgin Islands, U.S.",
                    "email": "Jairo_Moen@gmail.com",
                    "first_name": "Tevin",
                    "last_name": "Abbott",
                    "phone": "980.310.3714 x082",
                    "state": "Delaware",
                    "zip_code": "91034"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 75.97,
                "user": "Jasen68"
            },
            {
                "billing": {
                "items": {
                    "address": "6345 Stokes Burgs",
                    "city": "Walkerland",
                    "country": "Tokelau",
                    "email": "Toni39@gmail.com",
                    "first_name": "Santa",
                    "last_name": "Lowe",
                    "phone": "638.672.3654 x9750",
                    "state": "Wisconsin",
                    "zip_code": "59312"
                }
                },
                "cart": [
                {
                    "name": "T shirt 2",
                    "price": 25.99,
                    "quantity": 2
                },
                {
                    "name": "QR Code 1",
                    "price": 29.99,
                    "quantity": 1
                }
                ],
                "orderId": "7c542001-7ad5-4274-805e-44be6f117b95",
                "shipping": {
                "info": {
                    "items": {
                    "address": "6345 Stokes Burgs",
                    "city": "Walkerland",
                    "country": "Tokelau",
                    "email": "Toni39@gmail.com",
                    "first_name": "Santa",
                    "last_name": "Lowe",
                    "phone": "638.672.3654 x9750",
                    "state": "Wisconsin",
                    "zip_code": "59312"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 81.97,
                "user": "Bo_Huel32"
            },
            {
                "billing": {
                "items": {
                    "address": "2650 Lavinia Village",
                    "city": "Toms River",
                    "country": "Bosnia and Herzegovina",
                    "email": "Lincoln11@gmail.com",
                    "first_name": "Keagan",
                    "last_name": "Kub",
                    "phone": "331-348-8811",
                    "state": "Massachusetts",
                    "zip_code": "07577-9738"
                }
                },
                "cart": [
                {
                    "name": "T-shirt 1",
                    "price": 22.99,
                    "quantity": 5
                },
                {
                    "name": "NFT 1",
                    "price": 54.99,
                    "quantity": 1
                }
                ],
                "orderId": "997604b4-3119-4c4c-850e-67a28c00e62e",
                "shipping": {
                "info": {
                    "items": {
                    "address": "2650 Lavinia Village",
                    "city": "Toms River",
                    "country": "Bosnia and Herzegovina",
                    "email": "Lincoln11@gmail.com",
                    "first_name": "Keagan",
                    "last_name": "Kub",
                    "phone": "331-348-8811",
                    "state": "Massachusetts",
                    "zip_code": "07577-9738"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 169.94,
                "user": "Mariane44"
            },
            {
                "billing": {
                "items": {
                    "address": "053 Ward Loop",
                    "city": "Maxwellbury",
                    "country": "Chad",
                    "email": "Lulu21@hotmail.com",
                    "first_name": "Cielo",
                    "last_name": "Cronin",
                    "phone": "389-339-8218 x59125",
                    "state": "Utah",
                    "zip_code": "31851"
                }
                },
                "cart": [
                {
                    "name": "NFT 2",
                    "price": 54.99,
                    "quantity": 1
                },
                {
                    "name": "T shirt 2",
                    "price": 25.99,
                    "quantity": 1
                }
                ],
                "orderId": "8433f2f2-25ae-496f-b59a-3d73101ea382",
                "shipping": {
                "info": {
                    "items": {
                    "address": "053 Ward Loop",
                    "city": "Maxwellbury",
                    "country": "Chad",
                    "email": "Lulu21@hotmail.com",
                    "first_name": "Cielo",
                    "last_name": "Cronin",
                    "phone": "389-339-8218 x59125",
                    "state": "Utah",
                    "zip_code": "31851"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 80.98,
                "user": "Garth.Goyette"
            },
            {
                "billing": {
                "items": {
                    "address": "87076 Hauck Island",
                    "city": "West Saraiville",
                    "country": "Cocos (Keeling) Islands",
                    "email": "Frankie.Bode@hotmail.com",
                    "first_name": "Haylie",
                    "last_name": "Pagac",
                    "phone": "1-774-326-3365",
                    "state": "Rhode Island",
                    "zip_code": "21609-0773"
                }
                },
                "cart": [
                {
                    "name": "QR Code 1",
                    "price": 29.99,
                    "quantity": 6
                }
                ],
                "orderId": "1c46352a-bd66-4f42-954e-fe66dc120043",
                "shipping": {
                "info": {
                    "items": {
                    "address": "87076 Hauck Island",
                    "city": "West Saraiville",
                    "country": "Cocos (Keeling) Islands",
                    "email": "Frankie.Bode@hotmail.com",
                    "first_name": "Haylie",
                    "last_name": "Pagac",
                    "phone": "1-774-326-3365",
                    "state": "Rhode Island",
                    "zip_code": "21609-0773"
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "total": 179.94,
                "user": "Anais38"
            }
        ]
        for x in my_sample:
            x["cart"] = json.dumps(x["cart"])
            x["shipping"] = json.dumps(x["shipping"])
            x["billing"] = json.dumps(x["billing"])
            db.session.add(Order(**x))
        db.session.commit()

def init_users():
    in_db = User.query.all()
    if len(in_db) == 0:
        my_sample = [
            {
                "billing": {
                    "items": {
                        "address": "",
                        "city": "",
                        "country": "",
                        "email": "",
                        "first_name": "",
                        "last_name": "",
                        "phone": "",
                        "state": "",
                        "zip_code": ""
                    }
                },
                "myPass": "3Jvk7oziA4D67EZ",
                "shipping": {
                    "info": {
                        "items": {
                        "address": "",
                        "city": "",
                        "country": "",
                        "email": "",
                        "first_name": "",
                        "last_name": "",
                        "phone": "",
                        "state": "",
                        "zip_code": ""
                        }
                    },
                    "sameAsBilling": {
                        "checked": True
                    }
                },
                "user": "Marlen_Mayer"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "eIdkTxVzppjBSlu",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Judge35"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "BNUaKSuW0g6uhdR",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Nathanial_Pfeffer74"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "B_edfwpLbbCzkYx",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Allan_Murphy62"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "mAe4V5gNeOJYI37",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Maida.VonRueden17"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "zzKx4kV6FClgffe",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Michele74"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "DjgnhgARp2YfLfV",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Naomie4"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "RPCwpySmQ19MRRd",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Dan93"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "YehaIuyC1ZMbe3P",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Julio.Block"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "YlT4TaivprDztZz",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Maxine66"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "yK9OqWmkHyzGOp7",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Kamille98"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "cz5_scViqluxXYg",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Kaitlyn53"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "YVR_zQRcQmSlQOd",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Johnathon_Jerde12"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "teJw34OiVvryOXs",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Octavia.Kuphal"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "VPR1wRNtMKOqTY_",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Demetris.Fadel"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "Y41ybISpIgYPdIW",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Bailey92"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "E9Wn7Mdl_E9ulGh",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Kacey.Kuphal60"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "ktR3a1sV0x9Sz37",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Emile83"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "Vmra7SI2rDnMiAV",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Kathryne_Blanda3"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "b6Lje5_Bw0rFV3d",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Felipe.Trantow"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "vmM6fsL4GLTTibT",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Clifton23"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "93sbLYpn1f4TYJz",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Eriberto.Torphy"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "8F_sFYxHaKqS9yw",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Annie34"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "PYG_QzYFeKGFNgg",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Herbert_Herman"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "SbOi_1KbG9uFq_l",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Janice70"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "p9FRjBzo_l11kKq",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Dasia_Collins"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "25JwC3mzyflw4xx",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Bria.Pagac54"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "eweAjjyik6g8dqf",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Jamison.Funk"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "3_z3GZ6ltm7uUlj",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Hilda28"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "3U6U5ZLQhCyd4wp",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Hayley38"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "QQZSg34R6nLbif6",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Alexandro78"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "bGGo_2QXmHRchnQ",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Raegan_Fritsch50"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "2gC4sd47aSEk52P",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Helmer.Hilpert88"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "bTbjF84p5hwvO4i",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Katheryn_Lynch45"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "X0ObVMIWhh2fMdR",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Devante_Keeling"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "UfI5y9CrLPVF05q",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Jerrold35"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "GC4QiPqWMJQMbgw",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Mariam44"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "L6JOuGr4RT4X6xy",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Hardy_Stehr30"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "R6DzONNR0JSBJjd",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Georgette.Lubowitz27"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "UvYybcGZv61TZDO",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Loma.Leffler"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "wgXuRx0n2FmJCR6",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Pearlie.McGlynn68"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "wIezhrGYuf0o0oD",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Robert_Labadie32"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "8J6QIv43hThOykz",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Jasen68"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "5SIrx8qr9GqAIlT",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Gonzalo.Bauch"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "pT0BfgZrosXfRj9",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Dante31"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "W_qMddQJ9qQwOeV",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Bo_Huel32"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "dnVcT7m1InSCDmG",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Jaqueline.Schumm"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "F4dwwTcUxAxZewY",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Molly99"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "wg_FEtV8SDqsnfa",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Mariane44"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "7CnGSHBvZqfSDig",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Merlin.Flatley90"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "rvbF8MJRmj1k7mk",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Ed.Cruickshank"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "hdk6XwGnbUANdoO",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Garth.Goyette"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "SGfu9IueRM5lcvV",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Alexzander20"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "meHrna4KCOKUOuC",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Rebecca.Bergnaum1"
            },
            {
                "billing": {
                "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                }
                },
                "myPass": "8yekPcshS7sX4ud",
                "shipping": {
                "info": {
                    "items": {
                    "address": "",
                    "city": "",
                    "country": "",
                    "email": "",
                    "first_name": "",
                    "last_name": "",
                    "phone": "",
                    "state": "",
                    "zip_code": ""
                    }
                },
                "sameAsBilling": {
                    "checked": True
                }
                },
                "user": "Anais38"
            }
        ]
        for x in my_sample:
            x['shipping_same_as_billing'] = x['shipping']['sameAsBilling']['checked']
            x['billing'] = json.dumps(x['billing'])
            x['shipping'] = json.dumps(x['shipping'])
            
            db.session.add(User(**x))
        db.session.commit()

