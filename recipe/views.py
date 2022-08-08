from django.shortcuts import render, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import TemplateView
from .models import Recipe


class DeclinePage(generic.TemplateView):
    """Displays main page for site"""
    template_name = 'decline.html' 


class MainPage(generic.ListView):
    """Displays home page for site"""
    model = Recipe
    template_name = 'main.html'


class HomePage(generic.ListView):
    """Displays home page for site"""
    model = Recipe
    template_name = 'index.html'


class About(generic.TemplateView):
    """
    Displays information about the site
    """
    template_name = 'about.html'


class RecipesList(generic.ListView):
    """Displays view of all recipes """
    model = Recipe
    template_name = 'recipes.html'


class MyRecipes(generic.ListView):
    """Displays logged in Users Recipes"""
    model = Recipe
    template_name = 'my recipes.html'

