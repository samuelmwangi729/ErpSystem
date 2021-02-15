from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.Create,name="classes"),
    path('Class/New/Add',views.Add,name="addclass"),
    path('Class/Manage/All',views.Manage,name="classes.manage")
]
