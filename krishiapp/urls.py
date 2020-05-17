from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from django.conf.urls import url
from django.conf import settings
from krishiapp import views

from . import views

urlpatterns = [
    path('', views.indexView, name = "homepage"),
    path('secondpage/', views.secondPage, name = "secondpage"),
    path('cropslist', views.showCropsList),
    path('cropdetails/<int:cropid>', views.cropDetails, name = 'cropdetails')
]
# =======
#     path('crops/', views.cropList.as_view(), name= 'cropList'),
#     path('crops/<int:pk>/', views.cropDetail.as_view(), name='cropDetails'),
# >>>>>>> 805faf1512d25908e4e073d5f95c3dcfed4021af
# ]
