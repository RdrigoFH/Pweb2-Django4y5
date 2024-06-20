from django.urls import path
from . import views

urlpatterns = [
    path('crear_persona/', views.crear_persona, name='crear_persona'),
]
