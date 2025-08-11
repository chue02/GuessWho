from django.urls import path
from . import views

urlpatterns = [
    path("world", views.hello) # TODO: after creating paths with games views, delete this line.
]
