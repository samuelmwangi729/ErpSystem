from django.db import models

# Create your models here.
class StudentClass(models.Model):
    ClassNumber=models.IntegerField()
    Status=models.IntegerField(default=0)
    _createdAt=models.DateField(auto_now=False, auto_now_add=True)
    _updatedAt=models.DateField(auto_now=True, auto_now_add=False)
    _createdBy=models.CharField(max_length=30)
    _updatedBy=models.CharField(max_length=30,blank=True)