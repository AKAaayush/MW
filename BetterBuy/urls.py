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

from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('', views.laptos),
    path('laptos', views.laptos, name="laptos"),
    path('about', views.about, name="about"),
    path('apple', views.apple, name="apple"),
    path('userdetail', views.userdetail, name='userdetail'),
    path('admintable', views.admintable),

    # CRUD
    path('create', views.create, name="create"),
    path('loginvalid', views.loginvalid, name="loginvalid"),
    path('login', views.login, name="login"),
    path('adminentry', views.adminentry, name="adminentry"),
    # path('entry',views.entry),

    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),

    #     admin
    path('admindelete/<int:adminid>', views.admindelete),
    path('create1', views.create1),
    path('edit1/<int:adminid>', views.edit1),
    path('update1/<int:adminid>', views.update1),
    path('admin',views.adminlogin),
]
