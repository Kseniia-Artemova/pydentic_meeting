from pydantic import BaseModel, ValidationError
from pprint import pprint


class Cat(BaseModel):
    name: str
    age: int
    breed: str = "Беспородный"


class Dog(BaseModel):
    colors: list


cat = Cat(name="Барсик", age=3, breed="Сиамский")

# приводим данные к нужному формату
cat2 = Cat(name="Сема", age="2").model_dump()

print(cat)

# как __dict__, только с возможностью исключения лишних полей для выдачи
# м=или включения только нужных
print(cat.model_dump(exclude=("breed", )))
print(cat.model_dump(include=("age", "name")))

# `model_dump()   /   model_dump_json()`
# Возвращает словарь или словарь в строке

print(cat2)

# автоматически переводит кортеж в список
dog = Dog(colors=("red", "black"))
print(dog)

# `model_validate()` / `model_validate_json()`
# Используется для преобразования данных в словае / строке в экземпляр модели.

# cat = Cat.model_validate(name=3, age="4", breed=19)

cat_data = {"name": 4, "age": 3, "breed": 78}

try:
    cat = Cat(**cat_data)
except ValidationError as e:
    print(e)
    pprint(e.errors())
    print(e.error_count())

# except ValidationError as e:
#    print(e.errors()) # количество
#    print(e.error_count()) # все ошибки

# class Cat(BaseModel):
#
#     name: str = Field(... , min_length=2, max_length=7)
#     age: int = Field(... , gt=0, lt=20)
#
# cat_data = {"name": "Мурзик", "age": 30}
# cat = Cat(**cat_data)

# Полный список констрейнтов
#
# https://docs.pydantic.dev/dev-v2/usage/fields/



# Кастомная валидация на функциях
# from pydantic import BaseModel, field_validator
#
# class Cat(BaseModel):
#
#     name: str
#     age: int
#
#     @field_validator('age')
#     def must_be_between_0_and_20(cls, v):
#         if not 0 <= v <= 20:
#             raise ValueError('must be between 0 and 20')
#         return v
#
#
# cat_data = {"name": "Мурзик", "age": 30}
# cat = Cat(**cat_data)


