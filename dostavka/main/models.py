
from django.contrib.auth.hashers import make_password
from django.db import models

# Create your models here.
class User(models.Model):
    surname = models.CharField('Фамилия', max_length=60)
    name = models.CharField('Имя', max_length=25)
    patronymic = models.CharField('Отчество', max_length=45)
    email = models.CharField('Email', max_length=100)
    phone_number = models.CharField('Номер телефона', max_length=11)
    password = models.CharField('Пароль', max_length=150)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Order(models.Model):
    sender = models.CharField('Отправитель', max_length=100)
    senders_address = models.CharField('Адрес отправителя', max_length=150)
    shipped_item = models.CharField('Отправленный товар', max_length=150)
    FIO = models.CharField('ФИО', max_length=250)
    email = models.CharField('Email', max_length=100)
    phone_number = models.CharField('Номер телефона', max_length=11)
    address_recipient = models.CharField('Адрес получателя', max_length=150)


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'