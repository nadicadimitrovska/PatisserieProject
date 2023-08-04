from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Cakes(models.Model):
    title=models.CharField(max_length=50)
    ingredients=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"(self.title) (self.price)"


class Cookies(models.Model):
    title = models.CharField(max_length=50)
    ingredients = models.TextField()
    price = models.IntegerField()
    image=models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"(self.title) (self.price)"



class HealthyCookies(models.Model):
    title = models.CharField(max_length=50)
    ingredients = models.TextField()
    price = models.IntegerField()
    image=models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"(self.title) (self.price)"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cakes = models.ManyToManyField(Cakes, through='CartItem')
    cookies = models.ManyToManyField(Cookies, through='CartItem')
    healthycookies = models.ManyToManyField(HealthyCookies, through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    cakes = models.ForeignKey(Cakes, on_delete=models.CASCADE)
    cookies = models.ForeignKey(Cookies, on_delete=models.CASCADE)
    healthycookies = models.ForeignKey(HealthyCookies, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
