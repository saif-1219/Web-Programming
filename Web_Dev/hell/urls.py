from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path("saif", views.saif, name='saif'),
    path("<str:name>", views.greet, name="greet"),
    path("<str:name>/<str:color>", views.greet_with_color, name="greet")
]