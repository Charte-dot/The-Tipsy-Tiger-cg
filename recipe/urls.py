from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    path('decline/', views.DeclinePage.as_view(), name='decline'),
    path('home/', views.HomePage.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('recipelist/', views.RecipesList.as_view(), name='recipes'),
    path('myrecipes/', views.MyRecipes.as_view(), name='myrecipes'),

]