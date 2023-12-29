from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "Time/index.html",{
        "hour": (now.hour+5)%12,
        "minute": now.minute,
        "second": now.second,
    })