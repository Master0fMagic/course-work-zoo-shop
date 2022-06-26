import dto
import error
from setup import init_app

from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from flask_login import login_user, logout_user, login_required, current_user

from clientService import ClientService
from seller import OrderService, DeliveryService

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*", "supports_credentials": "true"}})
init_app(app)


@app.route('/api/login', methods=['POST'])
def login():
    """
    takes json: {
    "login":"user_email_or_phone_number",
    "password":"user_password"
    }

    creates user session
    :return: success or error
    """
    userdata = request.json['login']
    password = request.json['password']

    if not (userdata and password):
        abort(400, 'required field empty')

    cs = ClientService()
    try:
        user = cs.login(userdata, password)
        login_user(user)
    except (error.UseNotFoundException, error.WrongPasswordException) as er:
        abort(401, er.description)

    return jsonify(success=True)


@app.route('/api/logout', methods=['POST'])
@login_required
def logout():
    """
       ends user session
       :return: 200 ok
    """
    logout_user()
    return jsonify(success=True)


@app.route('/api/sing-up', methods=['POST'])
def sing_up():
    """
       takes json: {
       "email":"",  //field does not required
       "password":"",
       "repeated_password":"",
       "first_name":"",
       "last_name":"",
       "phone":"",
       }

       create new user and login him
       :return: success or error
       """
    email = '' if request.json.get('email') is None else request.json.get('email')
    password = request.json.get('password')
    repeated_password = request.json.get('repeated_password')
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    phone = request.json.get('phone')

    if not (password and repeated_password and first_name and last_name and phone):
        abort(400, 'missing required fields')

    if password != repeated_password:
        abort(400, 'passwords does not match')

    cs = ClientService()
    client = cs.register_new_user(first_name, last_name, phone, password, email)
    login_user(client)
    return jsonify(success=True)


@app.route('/api/order/create', methods=['POST'])
@login_required
def create_order():
    """
    takes json:{
    "address": "",
    "delivery_service_id": "",
    "items": [
        {
        "product_id":1,
        "amount": 1
        }
    ]

    }
    :return: 200
    """
    address = request.json.get('address')
    delivery_service_id = request.json.get('delivery_service_id')
    items = [dto.CreateOrderItemDto(id=item['product_id'], amount=item['amount']) for item in
             request.json.get('items')]

    if not (address and delivery_service_id and items):
        abort(400, 'not all fields persist')

    os = OrderService()
    os.create_order(address, delivery_service_id, items, current_user.id)
    return jsonify(success=True)


@app.route('/api/delivery-services')
@login_required
def get_delivery_services():
    """

    :return: {
    "data": [
        {
            "id": 1,
            "name": "Нова Пошта",
            "price": 75.0
        }
    }
    """
    ds = DeliveryService()
    return {
        'data': [item.to_dict() for item in ds.get_delivery_services()]
    }


@app.route('/api/order/categories')
@login_required
def get_categories():
    """

    :return: {
    "data": [
        {
            "id": 1,
            "name": "Корм для котів"
        }
        ]
    }
    """
    os = OrderService()
    return {
        'data': [item.to_dict() for item in os.get_categories()]
    }


@app.route('/api/products')
def get_products():
    """

    :return: {
     "data": [
        {
            "category": "Корм для котів",
            "category_id": 1,
            "description": "...",
            "id": 1,
            "name": "...",
            "price": 570.0,
            "image":"<link to image>"
        },
        ]
    }
   """
    os = OrderService()
    return {
        'data': [item.to_dict() for item in os.get_products()]
    }


@app.route('/api/order/history')
@login_required
def get_general_order_history():
    """
    :return:{
     "data": [
        {
            "address": "м.Харків, пр.Героїв Харкова, 27Б, 67",
            "date": 1655650779,
            "delivery_price": 70,
            "delivery_service": "Нова пошта",
            "discount": 0.0,
            "id": 2,
            "sum": 470.0,
            "sum_with_discount": 470.0,
            "total_sum": 540.0
        }
        ]
    }
    """
    os = OrderService()
    return {
        'data': [item.to_dict() for item in os.get_order_history(current_user.id)]
    }


@app.route('/api/order/history/<int:id>')
@login_required
def get_order_details(id: int):
    """
    :param id: order id
    :return: {
         "data": [
            {
                "amount": 1,
                "category": "Корм для котів",
                "description": "...",
                "name": "...",
                "price": 540.0,
                "image":"<link to image>"
            }
        ]
    }
    """

    os = OrderService()
    return {
        'data': [item.to_dict() for item in os.get_products_by_order(id)]
    }


app.run()
