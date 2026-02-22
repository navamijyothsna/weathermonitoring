from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('satellites/', views.satellites, name='satellites'),
    path('live-weather/', views.live_weather, name='live_weather'),
]

