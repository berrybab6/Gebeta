from django.urls import path
from . import views

urlpatterns = [
    path("aboutus",views.addchief, name="add chief"),
    path("",views.addfood,name="add food")
]
