from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic, View
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Views created here

from .models import *
from .forms import CreateUserForm


def SignUpPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

            context = {'form': form}
            return render(request, 'account/signup.html', context)


def LogInPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')

            context = {}
            return render(request, 'account/login.html', context)
        

def LogOutUser(request):
    logout(request)
    return redirect('login')      


class MainPage(generic.TemplateView):
    """Displays main page for site"""
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
