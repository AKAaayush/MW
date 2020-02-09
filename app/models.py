from django.db import models

class User(models.Model):
    user_id=models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    class Meta:
        db_table="userinfo"

# Home laptopadd
# class Addlaptop(models.Model):
#     # laptop_id = models.AutoField(auto_created=True, primary_key=True)
#     # name = models.CharField(max_length=100)
#     # img = models.ImageField(upload_to='img')
#     # desc = models.TextField()
#     # price = models.IntegerField
#     user_id = models.AutoField(auto_created=True, primary_key=True)
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     class Meta:
#         db_table="homelaptop"

# subscriber

# class Subscriber(models.Model):
#     id = models.AutoField(auto_created=True, primary_key=True)
#     email1 = models.CharField(max_length=100)
#
#     class Meta:
#        db_table="subsciber"

