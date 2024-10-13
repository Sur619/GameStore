import datetime
import uuid

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class ProductType(models.Model):
    type_name = models.CharField(max_length=200)

    class Meta:
        db_table = 'product_types'
        managed = False

    def __str__(self):
        return self.type_name


class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    class Meta:
        db_table = 'customers'
        managed = False


class Products(models.Model):
    name = models.CharField(max_length=255)
    type_id = models.ForeignKey(ProductType, on_delete=models.CASCADE, db_column='type_id', related_name='category')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'products'
        managed = False

    def __str__(self):
        return self.name


class Order(models.Model):
    order_date = models.DateTimeField('date published')
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='customer_id')

    class Meta:
        db_table = 'orders'
        managed = False


class Sale(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, db_column='product_id')
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, db_column='order_id')
    quantity = models.IntegerField(default=1)

    class Meta:
        db_table = 'sales'
        managed = False