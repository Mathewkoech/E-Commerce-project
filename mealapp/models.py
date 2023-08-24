from django.db import models
from django.urls import reverse

class Meal(models.Model):
    name  = models.CharField(max_length = 200)
    ingredients = models.CharField(max_length = 500, default=None)
    price = models.FloatField(null=True, blank=True,)
    image_url = models.CharField(max_length = 2083, default=False)
    meal_available = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)

    def __str__(self):
	    return self.name


class Order(models.Model):
	product = models.ForeignKey(Meal, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.product.name
