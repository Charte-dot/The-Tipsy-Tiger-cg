from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    path('index', views.Index.as_view(), name='home'),
]