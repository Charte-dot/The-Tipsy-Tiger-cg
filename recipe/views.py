# pylint: disable=locally-disabled, no-member

"""Imports"""
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Recipe
from .filters import RecipeFilter
from .forms import CommentForm


class MainPage(generic.ListView):
    """Displays home page for site"""
    model = Recipe
    template_name = 'main.html'


class DeclinePage(generic.TemplateView):
    """Displays main page for site"""
    template_name = 'decline.html'


class HomePage(generic.ListView):
    """Displays home page for site"""
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')[0:3]
    template_name = 'index.html'
    paginate_by = 4


class About(generic.TemplateView):
    """Displays information about the site"""
    template_name = 'about.html'


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
                "commented": False,
                "cheers": cheers,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        """shows full recipe with approved comments
        show if logged in user has given a cheers
        User can submit recipe for review to admin"""

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        cheers = False
        if recipe.cheers.filter(id=self.request.user.id).exists():
            cheers = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            messages.success(request, 'Thanks for your thoughts')
        else:
            comment_form = CommentForm()

        return render(
            request,
            'recipe_detail.html',
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "cheers": cheers,
                "comment_form": CommentForm()

            },
            )


class RecipesList(generic.ListView):
    """Displays view of all recipes """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes.html'

    def get_queryset(self):
        """filter cocktial by skill level and alcohol base"""
        queryset = super().get_queryset()
        filter = RecipeFilter(self.request.GET, queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        filter = RecipeFilter(self.request.GET, queryset)
        context["RecipeFilter"] = filter
        return context


class MyRecipes(LoginRequiredMixin, generic.ListView):
    """Displays logged in Users Recipes"""
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'myrecipes.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = context['recipe'].filter(author=self.request.user)

        return context


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


class RecipeCreate(
                    SuccessMessageMixin, LoginRequiredMixin,
                    generic.CreateView):
    """Logged in user can create a recipe and add it to their cocktail list"""

    model = Recipe
    fields = ['recipe_image', 'title', 'about', 'skill', 'base', 'serves',
              'ingredients', 'steps']
    template_name = 'recipe_form.html'
    success_url = reverse_lazy('myrecipes')
    success_message = "You have added a new cocktail to your list!"

    def form_valid(self, form):
        """Places logged in users as author and sets form to publish"""
        form.instance.author = self.request.user
        form.instance.status = 1

        return super(RecipeCreate, self).form_valid(form)


class RecipeEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    """ Logged in User can edit the cocktail recipe"""
    model = Recipe
    fields = ['recipe_image', 'title', 'skill', 'base', 'serves', 'about',
              'ingredients', 'steps', ]
    template_name = 'recipe_form.html'
    success_url = reverse_lazy('myrecipes')
    success_message = "You have Edited your cocktail!"


class RecipeDelete(SuccessMessageMixin, LoginRequiredMixin,
                   generic.DeleteView):
    """
    Logged in user can delete a recipe from their my recipes list
    """
    model = Recipe
    success_url = reverse_lazy('myrecipes')
    success_message = "Cocktail deleted!"

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(RecipeDelete, self).delete(request, *args, **kwargs)
