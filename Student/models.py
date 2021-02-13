from django.db import models

# Create your models here.
class Student(models.Model):
    FirstName=models.CharField(max_length=30,blank=False,null=False)
    SecondName=models.CharField(max_length=30,blank=False,null=False)
    Surname=models.CharField(max_length=30,blank=False,null=False)
    Class=models.IntegerField(default=0)
    Stream=models.CharField(max_length=30,blank=False,null=False)
    Dob= models.DateField(auto_now=False, auto_now_add=False)
    ParentName=models.CharField(max_length=30,blank=False,null=False)
    ParentContact =models.CharField(max_length=30,blank=False,null=False)
    EmergencyContact=models.CharField(max_length=30,blank=False,null=False)
    ParentEmail= models.EmailField(max_length=30)
    HomeCounty=models.CharField(max_length=30,blank=False,null=False)
    District=models.CharField(max_length=30,blank=False,null=False)
    Location=models.CharField(max_length=30,blank=False,null=False)
    DoA= models.DateField(auto_now=False, auto_now_add=True)
    Kcpe=models.IntegerField(default=0)
    Dormitory=models.CharField(max_length=30,blank=False,null=False)
    Clubs=models.CharField(max_length=30,blank=False,null=False)
    Others=models.TextField(max_length=30,blank=False,null=False)
    Passport=models.ImageField(upload_to='StudentImages')
    Status=models.IntegerField(default=1)
    _createdAt=models.DateField(auto_now=False, auto_now_add=True)
    _updatedAt=models.DateField(auto_now=True, auto_now_add=False)
    _updatedBy=models.CharField(max_length=30)

class StudentClass(models.Model):
    ClassName=models.CharField(max_length=2)
    Status=models.IntegerField(max_length=2)
    ClassNumber=models.OneToOneField("Student", on_delete=models.PROTECT)