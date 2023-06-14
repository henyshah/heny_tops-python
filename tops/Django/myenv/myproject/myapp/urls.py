"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about')
]


# django follows MVT architecture:
# M - Model
# V - View
# T - Template


"""
model: it contains all the tables which we can connect with the database.
view:view.py file which is connected with specific application url
templates:which can contain  all the html web pages

urls.py:project level which is connected with the specific application url 
urls.py:app level which is connected with the specific views
"""

class User(models.Model):
    email=models.Emailfield(unique=True,max_length=30)
    password=models.Charfield(unique=True,max_length=30)
    role=models.Charfield(unique=True,max_length=20)
    created_at=modles.DateTimeField(auto_created=True)
    is_login=models.BooleanField(default=False)