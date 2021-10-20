from django.db import models


class Person(models.Model):
    s = (("F", "Female"), ("M", "Male"))
    name = models.CharField(max_length=11, verbose_name='Имя')
    surname = models.CharField(max_length=11, verbose_name='Фамилия')
    date_of_birth = models.IntegerField()
    gender = models.CharField(max_length=5, choices=s)
