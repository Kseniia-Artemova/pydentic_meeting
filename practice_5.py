from pydantic import BaseModel, Field, computed_field

# Создайте модель `Group` ,
#
# name - строка
#
# students – студенты класса Student
#
# Вычисляемые поля
#
# количество студентов - число
#
# средняя оценка - число
#
#  у создайте вложенную модель `Student`
#
# name - имя студента
#
# grade -оценка студента
#
# Верните плоский объект без студентов но с информацией


class Student(BaseModel):
    name: str
    grade: int = Field(..., ge=0, le=100)


class Group(BaseModel):
    name: str
    students: list[Student] = Field(..., exclude=True)

    @computed_field()
    @property
    def students_number(self) -> int:
        return len(self.students)

    @computed_field()
    @property
    def average_grade(self) -> float:
        average_grade = sum([student.grade for student in self.students])/self.students_number
        return round(average_grade, 0)


group = Group(name="My group", students=[Student(name="Kate", grade=88),
                                         Student(name="Renat", grade=91),
                                         Student(name="Misha", grade=64)])
result = group.model_dump()
print(result)