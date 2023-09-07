from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.views.generic.base import View
# class SignUpView(View):
#     def get(self, request):
#         form = SignUpForm(request.POST or None)
#         return render(request, 'signup.html', {'form': form})

#     def post(self, request):
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login/')
#         return render(request, 'signup.html', {'form': form})

class SignUpView(generic.CreateView):
    form_class    = UserCreationForm
    success_url   = reverse_lazy('login')
    template_name = 'signup.html'