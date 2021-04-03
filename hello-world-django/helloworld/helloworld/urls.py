"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

     path('homepage/', include('myapp.urls')),
    path('homepage2/', include('myapp.urls')),
    path('rango/index.html/', include('myapp.urls')),
    path('your-name/', include('myapp.urls')),
    path('test/', include('myapp.urls')),
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
   
    path('', include('myapp.urls')),

    # so i think views correspond to urls somehow...
    # would we have one of these fofr every page?

    path('admin/', admin.site.urls),
]
