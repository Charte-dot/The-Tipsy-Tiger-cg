from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import AgeCheck, NewUserForm
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


def register_request(request):
    if request.method == "Post":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration sucessful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration.Invalid Info")
    form = NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form":form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")
