from django.urls import path
from . import views

# URL Configuration
urlpatterns = [
    # /movies, we use '' because of root of movies app
    path('', views.index, name='index')
]
