from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    path('home/', views.HomePage.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('recipelist/', views.RecipesList.as_view(), name='recipes'),
    path('myrecipes/', views.MyRecipes.as_view(), name='myrecipes'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('cheers/<slug:slug>', views.RecipeCheers.as_view(),
         name='recipe_cheers'),


]