from django.db import models

# Create your models here.
class Streams(models.Model):
    stream=models.CharField(max_length=20,blank=False)
    Status=models.IntegerField()
    _createdAt=models.DateField(auto_now=False,auto_now_add=True)
    _updatedAt=models.DateField(auto_now=True,auto_now_add=False)