from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from django.conf.urls import url
from django.conf import settings
from krishiapp import views

urlpatterns = [
    # path('', views.index, name= 'HomePage'),
    path('crops/', views.cropList.as_view(), name= 'cropList'),
    path('crops/<int:pk>/', views.cropDetail.as_view(), name='cropDetails'),
] 