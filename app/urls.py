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
    path('entry', views.entry, name="entry"),
    # path('entry',views.entry),

    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),

    #  admintabel controle panel
    path('admindelete/<int:adminid>', views.admindelete),
    path('create1', views.create1),
    path('edit1/<int:adminid>', views.edit1),
    path('update1/<int:adminid>', views.update1),

    # adminlogin

]
