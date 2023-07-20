from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Category Model

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True , blank = True)
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    add_date = models.DateTimeField(auto_now_add=True, null=True)

#Post Model

# class Post(models.Model):
#     post_id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     url = models.CharField(max_length=100)
#     cat = models.ForeignKey(Category, on_delete=models.CASCADE)


