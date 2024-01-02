from django.urls import path

from . import views

urlpatterns = [
    path("edit_page/", views.edit_page, name="edit_page"),
    path("save/", views.save, name="save"),
    path("random/", views.random_page, name="random"),
    path("search/", views.search, name="search"),
    path("new_page/", views.new_page, name="new_page"),
    path("<str:title>/", views.title, name="title"),
    path("", views.index, name="index"),
]
