# from django.http import HttpResponse
from django.shortcuts import render

from .models import City

# Create your views here.


def cities(request):

    city_names = City.objects.all()

    context = {

        "city_names": city_names

    }
    return render(request, "main/cities.html", context)
