from django.http import HttpResponse
from django.shortcuts import render
from contact.models import PeopelInfo

# Create your views here.


def index(request):
    return HttpResponse("Welcom to my App!")


def home(request):
    people_list = PeopelInfo.objects.all()
    # queryset结构：[{k:v, "name': "Tom"}, {}, {}]
    # people_info = {"name": ""}
    # context = {"people": people_info, "people_list": ["Tim", "Alice", "Merry"]}
    context = {"people_list": people_list}
    return render(request, "contact/index.html", context=context)


def detail(request, name):
    people = PeopelInfo.objects.filter(name=name)[0]
    print(people.name)
    print(people.age)
    print(people.phone_number)
    context = {"people": people}
    return render(request, "contact/detail.html", context=context)