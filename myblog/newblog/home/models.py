
from django.db import models

# Create your models here.
class Contact(models.Model):
    serialno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    # phone=models.CharField(max_length=14)
    email=models.CharField(max_length=150)
    content=models.TextField()
    # timeStamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'Message form ' + self.name