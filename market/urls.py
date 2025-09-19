from django.urls import path
from . import views

urlpatterns = [
    # ejemplo mínimo
    path("", views.home, name="home"),
]