from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util
import random

class AddTextForm(forms.Form):
    title = forms.CharField(label="Add Title")
    text = forms.CharField(widget=forms.Textarea)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def new_page(request):
    if request.method == "POST":
        title = request.POST['page_title']
        content = request.POST['content']
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/new_page.html", {
                "error":True
            })
        else:
            util.save_entry(title, content)
            # return HttpResponseRedirect(reverse("wiki:index"))
            return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries()
            })
    else:
        return render(request, "encyclopedia/new_page.html",{
            "error":False
        })


def title(request, title):
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "content": util.get_entry(title)
    })

def edit_page(request):
    if request.method == "POST":
        title = request.POST['page_title']
        return render(request, "encyclopedia/edit_page.html", {
            "title": title,
            "content": util.get_entry(title)
        })

def save(request):
    if request.method == "POST":
        title = request.POST['page_title']
        content = request.POST['content']
        util.save_entry(title, content)
        return render(request, "encyclopedia/title.html", {
            "title": title,
            "content": util.get_entry(title)
        })

def random_page(request):
    entries = util.list_entries()
    length = len(entries)
    num = random.randint(0, length-1)
    title = entries[num]
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "content": util.get_entry(title)
    })

def search(request):
    if request.method == "POST":
        entry = request.POST['entry']
        lst = util.list_entries()
        if entry in lst:
            return render(request, "encyclopedia/title.html", {
            "title": entry,
            "content": util.get_entry(entry)
        })
        else:
            subs = []
            for i in lst:
                if entry in i:
                    subs.append(i)
            return render(request, "encyclopedia/search_res.html", {
                "subs":subs,
                "empty":len(subs) == 0
            })