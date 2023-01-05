from django.db import models

# Create your models here.

"""
Пример простой модели, для создание модели можно создать класс и унаследовать Model
далее добавить атрибуты в класс как в примере, на основе этих атрибутов будут создаваться
столбцы в таблицы

После того как модель была прописана можно создать миграции, перед этим надо добавит приложение если не добавленно
в список INSTALLED_APPS в settings

>>> python3 manage.py makemigrations

Далее надо запустить миграции 

>>> python3 manage.py migrate

"""


class Student(models.Model):
    """
    Student data of all students in school
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
