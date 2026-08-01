from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.menu, name="menu"),
    path('/add', views.add_, name="add"),
]
