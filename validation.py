from pydantic import BaseModel, Field, ValidationError, field_validator
from pprint import pprint


class Cat(BaseModel):

    name: str = Field(... , min_length=20, max_length=7)
    age: int = Field(... , gt=0, lt=20)
# Полный список констрейнтов
#
# https://docs.pydantic.dev/dev-v2/usage/fields/


try:
    cat_data = {"name": "Мурзик", "age": 30}
    cat = Cat(**cat_data)
except ValidationError as e:
    pprint(e.errors())


class Dog(BaseModel):

    name: str
    age: int

# ValidationError наследуется от ValueError
# Если нужна другая ошибка, можно свою создать
    @field_validator('age')
    def must_be_between_0_and_20(cls, v):
        if not 0 <= v <= 20:
            raise ValueError('must be between 0 and 20')
        return v

# Можно применять валидатор к нескольким полям
# @field_validator('foo', 'boo')

try:
    dog_data = {"name": "Мурзик", "age": 30}
    dog = Dog(**dog_data)
except ValidationError as e:
    pprint(e.errors())