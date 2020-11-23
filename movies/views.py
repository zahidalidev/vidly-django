from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

# Create your views here.


def index(request):
    # Movie.objects.filter(release_year=1984)  # filtering
    # Movie.objects.get(id=1)  # getting single movie object with the id
    movies = Movie.objects.all()  # to get all the movies objects

    return render(request, 'movies/index.html', {'movies': movies})
    # return HttpResponse(output)
