from django.urls import path
from potosioBackend import views

urlpatterns = [
    path('', views.home, name="home"),
]
