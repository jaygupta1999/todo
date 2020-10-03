from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("bri",views.bri, name="brian"),
    path("<str:name>", views.greet, name="greet")
]


