from django.shortcuts import render
from django.views import generic
from .models import Recipe


class MainPage(generic.TemplateView):
    """Displays main page for site"""
    template_name = 'main.html'
