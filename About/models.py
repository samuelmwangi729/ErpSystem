from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=100, blank=False)
    Tag=models.TextField(blank=False)
    About=models.TextField(blank=False)
    Logo=models.ImageField(upload_to='pictures')