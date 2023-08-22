# ### Практика на Computed
#
# Напишите класс Homework у которого есть поля
#
# `student`
#
# `score`
#
# `lesson`
#
# Добавьте вычисляемые поля
#
# `grade` (A если score ≥ 80,  B если score ≥ 50, иначе C)
#
# `course` (если урок 1-9 это первый курс, если 10-19 это второй, 20-29 это третий)
#
# Подсказка // 10 даст курс


from pydantic import BaseModel, Field, ValidationError, field_validator, computed_field
from pprint import pprint
from typing_extensions import Annotated


class Homework(BaseModel):
    student: str
    score: int = Field(ge=0, le=100)
    lesson: int = Field(gt=0, le=29)

    @computed_field
    @property
    def grade(self) -> str:
        if self.score >= 80:
            return 'A'
        elif self.score >= 50:
            return 'B'
        else:
            return 'C'

    @computed_field
    @property
    def course(self) -> str:

        COURSES = {
            1: 'первый курс',
            2: 'второй курс',
            3: 'третий курс'
        }

        return COURSES.get(self.lesson // 10 + 1)


homework = Homework(student="Sergei", score=85, lesson=29)
result = homework.model_dump()
print(result)



