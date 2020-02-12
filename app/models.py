from django.db import models


class User(models.Model):
    user_id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "userinfo"


class Subcriber(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    subemail = models.CharField(max_length=100)

    class Meta:
        db_table = "subscriber"


class Admin(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    adminname = models.CharField(max_length=100)
    adminemail = models.CharField(max_length=100)
    adminpassword = models.CharField(max_length=100)

    class Meta:
        db_table = "adminuser"


