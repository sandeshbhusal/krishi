from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.indexView, name = "homepage"),
    path('secondpage/', views.secondPage, name = "secondpage"),
    path('cropslist', views.showCropsList)
]
