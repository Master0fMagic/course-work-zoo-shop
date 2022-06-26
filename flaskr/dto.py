from flask_login import UserMixin
from dataclasses import dataclass


@dataclass()
class Client(UserMixin):
    id: int
    firstname: str
    lastname: str
    email: str
    phone_number: str
    password: str


@dataclass()
class CreateOrderItemDto:
    id: int
    amount: int


@dataclass()
class DeliveryService:
    id: int
    name: str
    price: float

    def to_dict(self):
        return self.__dict__


@dataclass()
class Filter:
    id: int
    name: str

    def to_dict(self):
        return self.__dict__


@dataclass()
class Product:
    id: int
    name: str
    description: str
    price: float
    category_id: int
    category: str
    image: str

    def to_dict(self):
        return self.__dict__


@dataclass()
class Order:
    id: int
    date: int
    sum: float
    discount: float
    sum_with_discount: float
    address: str
    delivery_service: str
    delivery_price: float
    total_sum: float

    def to_dict(self):
        return self.__dict__


@dataclass()
class OrderProductInfo:
    name: str
    category: str
    description: str
    price: float
    amount: int

    def to_dict(self):
        return self.__dict__
