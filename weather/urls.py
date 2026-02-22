from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('satellites/', views.satellites, name='satellites'),
]

