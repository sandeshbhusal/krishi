from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView),
    path('cropslist', views.showCropsList)
]