from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView),
    path('secondpage/', views.secondPage, name = "secondpage")
]