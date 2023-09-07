from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('econ_auth/', SignUpView.as_view(), name = 'signup'),
]
