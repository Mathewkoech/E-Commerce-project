from datetime import datetime
from django.db import models
from django.urls import reverse
import uuid

def generate_slug():
    return str(uuid.uuid4())

class Meal(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    image_url = models.URLField()
    meal_available = models.BooleanField()
    quantity = models.IntegerField()
    meal_type = models.CharField(max_length=255,null=False,default="Unknown")
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

    def __str__(self):
	    return self.name


class Order(models.Model):
	product = models.ForeignKey(Meal, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(default=datetime.now()) 
	total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

	def __str__(self):
		return self.product.name

	def update_total_price(self):
		self.total_price = sum(meal.price for meal in self.meals.all())
		self.save()
