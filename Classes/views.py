from django.shortcuts import render,redirect
from django.contrib import messages
from .models import StudentClass
# Create your views here.
def Create(request):
    return render(request,'Class.html')

def Add(request):
    if request.method == 'POST':
        classname=request.POST['ClassName']
        if len(classname)==0:
            messages.info(request,'The Class Value cant be empty')
            return redirect('classes')
        else:
            #means that the value is not null
            print(classname)
            #look if the class already exists
            if StudentClass.objects.filter(ClassNumber=classname).exists():
                #then the class already exists 
                messages.error(request,'The class already exists')
                return redirect('classes')
            is_class_created=StudentClass.objects.create(ClassNumber=classname)
            if is_class_created: 
                messages.success(request,'Class Successfully Created')
                return redirect('classes')
    else:
        return redirect('classes')
def Manage(request):
    #first get all the classes here 
    Classes=StudentClass.objects.all() # fetched all the classes from the database
    return render(request,'ManageClass.html',{'Classes':Classes})