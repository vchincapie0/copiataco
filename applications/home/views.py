from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy

# Create your views here.

class Home(LoginRequiredMixin, TemplateView):
    template_name = "home/inicio.html"
    login_url=reverse_lazy('users_app:login')
