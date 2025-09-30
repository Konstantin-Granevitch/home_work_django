from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField()
    image = models.


class Category(models.Model):
    pass
