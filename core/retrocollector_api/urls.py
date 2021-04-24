from django.urls import path

from . import views
urlpatterns = [
    path("/", views.collectible_api),
    path("/<int:pk>", views.collectible_api),
]