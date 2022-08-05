from django.shortcuts import render, get_object_or_404, reverse
from django.shortcuts import render
from django.views import generic, View
from django.views.generic import TemplateView, CreateView
from .forms import AgeCheck
from django.urls import reverse_lazy
from .models import Recipe


class MainPage(generic.TemplateView):
    """Displays main page for site"""
    template_name = 'main.html'


class AgeCheckView(CreateView):
    """Displays age check on main page"""
    form_class = AgeCheck
    sucess_url = reverse_lazy('main')
    template_name = 'main.html'
    

class Index(generic.ListView):
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