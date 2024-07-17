from django.urls import path

from . import views

urlpatterns = [
    path('', views.ChessPlay, name='ChessPlay'),
]
