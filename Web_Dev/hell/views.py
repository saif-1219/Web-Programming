from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def saif(request):
    return HttpResponse("Hello, Saif")

def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })

def greet_with_color(request, name, color):
    return render(request, "hello/greet.html",{
        "name": name.capitalize(),
        "color": color
    })