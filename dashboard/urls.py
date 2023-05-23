from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('2', views.dashboard2),
    path('3', views.dashboard3)
]
