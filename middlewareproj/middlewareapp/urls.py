from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home),
    path("", views.hello, name="hello"),
    path("1/", views.some_view),
]