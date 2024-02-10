from django.urls import path

from . import views

urlpatterns= [
    path("", views.index, name='index'),
    path("year/1960/", views.index1, name='index1'),
    path("dob/1-1-1960/", views.index2, name='index2'),
]