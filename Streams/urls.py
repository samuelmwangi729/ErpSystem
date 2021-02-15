from django.urls import path 
from  . import views 

urlpatterns = [
    path('',views.Index,name='stream'),
    path('Add/New',views.New,name='addstream'),
]
