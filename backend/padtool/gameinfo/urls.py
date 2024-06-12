from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:monster_id>/", views.monster, name="monster"),
]