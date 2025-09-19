from django.urls import path
from perfil.views import edit_profile, profile_view

urlpatterns = [
    path('', profile_view, name='profile'),              # /perfil/
    path('editar/', edit_profile, name='edit_profile'),  # /perfil/editar/
]