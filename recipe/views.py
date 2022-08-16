from django.shortcuts import render, reverse, get_object_or_404
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
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
    

class RecipeInfo(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        cheers = False
        if post.cheers.filter(id=self.request.user.id).exists():
            cheers = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "cheers": cheers
            }
        ) 


class About(generic.TemplateView):
    """
    Displays information about the site
    """
    template_name = 'about.html'


class RecipesList(generic.ListView):
    """Displays view of all recipes """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes.html'
    paginate_by = 6


class MyRecipes(generic.ListView):
    """Displays logged in Users Recipes"""
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'my recipes.html'
    context_object_name = 'recipe'

