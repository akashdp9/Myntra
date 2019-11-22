from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default='media/default.jpg',upload_to='media')


    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(default='media/default.jpg',upload_to='media')
    brand = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def unit_price(self):
        return self.item.price

    def bill(self):
        cart_value = self.quantity * self.item.price
        return cart_value

    is_cancelled = models.BooleanField(default=False, null=True)

