from django.urls import path

from . import views
urlpatterns = [
    path("collectibles", views.collectible_api),
    path("collectibles/<int:pk>", views.collectible_api),
    path('types', views.type_api),
    path('types/<int:pk>', views.type_api)
]