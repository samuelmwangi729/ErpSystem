from django.shortcuts import render
from  .models import About

# Create your views here.
def Index(request):
    context=About.objects.all()
    return render(request,'Index.html',{'Context':context})
def Index2(request):
    return render(request,'Index2.html',{'name':'Homepage'})