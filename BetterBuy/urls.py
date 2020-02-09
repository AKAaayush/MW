"""BetterBuy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from app import views

urlpatterns = [
    path('', views.index),
    # path('', views.laptos),
    path('laptos', views.laptos,name="laptop"),
    path('about', views.about, name="about"),
    path('apple', views.apple, name="aplle"),
    path('dashbord', views.dashbord, name="dashbord"),

    # CRUD
    path('create',views.create),
    path('login',views.login),
    path('entry',views.entry),

    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
    path('',include("app.urls") )

]
