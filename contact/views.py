from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Welcom to my App!")


def home(request):
    return render(request, "contact/index.html")