from xmlrpc.client import NOT_WELLFORMED_ERROR
from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    serialno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=250)
    content=models.TextField()
    auther=models.CharField(max_length=150)
    slug=models.CharField(max_length=150)
    image=models.ImageField(upload_to='blogpage/')
    timeStamp=models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.title + ' by ' + self.auther