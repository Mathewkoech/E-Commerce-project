from django.shortcuts import render 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Meal, Order
from django.urls import reverse_lazy
from django.db.models import Q # for search method
from django.http import JsonResponse
import json
from django.contrib.auth.mixins import LoginRequiredMixin



class MealsListView(ListView):
    model = Meal
    template_name = 'list.html'


class MealsDetailView(DetailView):
    model = Meal
    template_name = 'detail.html'


class SearchResultsListView(ListView):
	model = Meal
	template_name = 'search_results.html'

	def get_queryset(self): # new
		query = self.request.GET.get('q')
		return Meal.objects.filter(
		name__search=query,
		meal_type__search=query
		)

class MealCheckoutView(DetailView):
    model = Meal
    template_name = 'checkout.html'

    from django.contrib.auth.mixins import LoginRequiredMixin 

class BookCheckoutView(LoginRequiredMixin, DetailView):
    model = Meal
    template_name = 'checkout.html'
    login_url     = 'login'


# def paymentComplete(request):
# 	body = json.loads(request.body)
# 	print('BODY:', body)
# 	product = Meal.objects.get(id=body['productId'])
# 	Order.objects.create(
# 		product=product
# 	)
# 	return JsonResponse('Payment completed!', safe=False)

def login_view(request):
  form = LoginForm(request.POST)

  if form.is_valid():
    ...
