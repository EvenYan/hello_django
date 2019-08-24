from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Welcom to my App!")


def home(request):
    people_info = {"name": ""}
    context = {"people": people_info, "people_list": ["Tim", "Alice", "Merry"]}
    return render(request, "contact/index.html", context=context)