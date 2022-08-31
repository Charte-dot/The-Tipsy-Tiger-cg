from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('recipe.urls'), name='recipe_urls'),
    path('accounts/', include('allauth.urls')),

]

handler404 = 'thetipsytiger.views.handler404'
handler500 = 'thetipsytiger.views.handler500'
