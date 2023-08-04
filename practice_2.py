from pydantic import BaseModel, Field, ValidationError, field_validator
from decimal import Decimal
from pprint import pprint


# Напишите модель  Order (Заказ), которая будет содержать поля:
#
# `pk` – int – первичный ключ
#
# **`customer_name`** – str(до 32) – имя заказчика
#
# **`customer_address`** – str(до 64) – адрес заказчика
#
# **`items`** – непустой список товаров с их количеством
#
# **`total_price`** – decimal – общая стоимость заказа, больше 0
#
# Напишите функцию, которая получает данные из словаря и возвращает количеств ошибок


class Order(BaseModel):
    pk: int
    customer_name: str
    customer_address: str
    items: list
    total_price: Decimal

    @field_validator('customer_name')
    def must_be_less_32(cls, v):
        if len(v) > 32:
            raise ValueError('must be less 32')
        return v

    @field_validator('customer_address')
    def must_be_more_64(cls, v):
        if len(v) > 32:
            raise ValueError('must be less 64')
        return v

    @field_validator('items')
    def must_be_not_empty(cls, v):
        if not v:
            raise ValueError('must be not empty')
        return v

    @field_validator('total_price')
    def must_be_more_0(cls, v):
        if v < 0 or type(v) is not Decimal:
            raise ValueError('must be more 0')
        return v


data = {"pk": 2,
        "customer_name": "Абрахаим",
        "customer_address": "//////////////////////////",
        "items": [6],
        "total_price": 16}

print(data)

try:
    order = Order(**data)
    print(order)
except ValidationError as e:
    pprint(e.errors())
    print(e.error_count())

