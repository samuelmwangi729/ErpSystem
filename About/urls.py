from django.urls import path
from . import views 

urlpatterns = [
    path('',views.Index,name="Home Page"),
    path('Demo',views.Index2,name="Home Page2"),
]
