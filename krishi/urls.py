"""krishi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import include, path 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('krishiapp.urls')),
=======
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('krishiapp.urls'))
>>>>>>> 183b360e2a4d3a4ae1de9786b8f2751b7b3b6de1
]
