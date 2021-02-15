from django.shortcuts import render,redirect
from Classes.views import StudentClass
from django.contrib import messages
from .models import Streams
# Create your views here.
def Index(request):
    return render(request,'Class.html',{'Classes':StudentClass.objects.all() })
def New(request):
    if request.method =='POST':
        #thne the method is right 
        #check if the value is empty
        streamname=request.POST['StreamName']
        if len(streamname) == 0:
            messages.error(request,'The Stream  Name must not  be empty')
            return redirect('classes')
        else:
            #check if the stream exists 
            if Streams.objects.filter(stream=streamname).exists():
                #then this is dublicate and should not be allowed 
                messages.info(request,'The stream has already been added. You can not add a dublicate')
                return redirect('classes')
            else:
                #then we  need to save the details to the database 
                stream=Streams.objects.create(stream=streamname,Status=0)
                if stream:
                    messages.info(request,'The Stream Has been successfully Created')
                    return redirect('classes')
                else:
                    messages.info(request,'Unknown error occurred')
                    return redirect('classes')
    else:
        messages.error(request,'the method is not needed here.')
        return redirect('classes')