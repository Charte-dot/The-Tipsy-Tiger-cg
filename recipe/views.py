from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Recipe
from .filters import RecipeFilter


class MainPage(generic.ListView):
    """Displays home page for site"""
    model = Recipe
    template_name = 'main.html' 
    

class HomePage(generic.ListView):
    """Displays home page for site"""
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')[0:3]
    template_name = 'index.html'
    paginate_by = 6 
    

class RecipeDetail(LoginRequiredMixin, View):
    """Displays the full cocktail recipe to logged in users"""

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        cheers = False
        if recipe.cheers.filter(id=self.request.user.id).exists():
            cheers = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
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
    
    """filter cocktial by skill level and alcohol base"""
    def get_queryset(self):
        queryset = super().get_queryset()
        filter = RecipeFilter(self.request.GET, queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        filter = RecipeFilter(self.request.GET, queryset)
        context["RecipeFilter"] = filter
        return context


class MyRecipes(generic.ListView):
    """Displays logged in Users Recipes"""
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'myrecipes.html'
    context_object_name = 'recipe'



class RecipeCheers(LoginRequiredMixin, View):
    """ Logged in Users can cheer/like a cocktial"""

    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.cheers.filter(id=self.request.user.id).exists():
            recipe.cheers.remove(request.user)
            messages.info(request, 'You have removed your cocktail cheer!')
        else:
            recipe.cheers.add(request.user)
            messages.success(request, 'You gave this cocktail a cheers!')

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))     

