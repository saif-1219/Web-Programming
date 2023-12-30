from django.shortcuts import render
import random
# Create your views here.

def index(request, name = ""):
    num = random.randint(0,1)
    return render(request, "Luck/index.html", {
        'luck': num,
        'name': name.capitalize()
        })
