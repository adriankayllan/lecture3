from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("adrian/", views.adrian, name="adrian"),
    path("<str:nome>/", views.saudacao, name="saudacao")
]