from pydantic import BaseModel


# Практика 1
# Создайте модель **Vacancy (Вакансия)**
#
# `pk` – int
#
# `title` – str
#
# `description` – str - по умолчанию “”
#
# Создайте 3 модельки с данными
#
# 1 – Аналитик – считает цифры
#
# 2 – Тестировщик  – проверяет работу программы
#
# 3 – Менеджер – за всеми присматривает


class Vacancy(BaseModel):
    pk: int
    title: str
    description: str = ""


analitic = Vacancy(pk=1, title="Аналитик", description="Считает цифры")
tester = Vacancy(pk=2, title="Тестировщик", description="Проверяет работу программы")
manager = Vacancy(pk=3, title="Менеджер", description="За всеми присматривает")

print(analitic, tester, manager, sep="\n")