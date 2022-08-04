from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, CreateView
from .forms import AgeCheck
from django.urls import reverse_lazy
from .models import Recipe


class MainPage(generic.TemplateView):
    """Displays main page for site"""
    template_name = 'main.html'


class AgeCheckView(CreateView):
    form_class = AgeCheck
    sucess_url = reverse_lazy('main')
    template_name = 'recipe/main.html'