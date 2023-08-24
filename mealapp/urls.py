from django.urls import path
from .views import MealsListView, MealsDetailView, MealCheckoutView, SearchResultsListView


urlpatterns = [
    path('', MealsListView.as_view(), name = 'list'),
    path('<int:pk>/', MealsDetailView.as_view(), name = 'detail'),
    path('<int:pk>/checkout/', MealCheckoutView.as_view(), name = 'checkout'),
    path('search/', SearchResultsListView.as_view(), name = 'search_results'),
    #path('complete/', paymentComplete, name = 'complete'),
]