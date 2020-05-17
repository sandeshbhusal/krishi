from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.index, name= 'HomePage'),
    path('', views.indexView),
    path('cropslist', views.showCropsList)
]

