from django.db import models

class User(models.Model):
    user_id=models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    class Meta:
        db_table="userinfo"