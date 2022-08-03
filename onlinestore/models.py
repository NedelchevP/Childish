from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField()


class Orders(models.Model):
    date = models.DateField()
    products = models.ManyToManyField(Product)
