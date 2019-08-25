from django.http import HttpResponse
from django.shortcuts import render, redirect
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


def register(request):
    return render(request, "contact/register.html")


def save_data(request):
    name = request.POST.get("name")
    age = request.POST.get("age")
    phone_number = request.POST.get("phone_number")
    print(name, age, phone_number)
    if name:
        PeopelInfo.objects.create(name=name, age=age, phone_number=phone_number)
        return HttpResponse("数据%s保存成功" % name)
    return redirect("/contact/register")
