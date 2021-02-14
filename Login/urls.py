from django.urls import path
from . import views

urlpatterns=[
    path('',views.Login,name="login"),
    path('Account/Logout',views.Logout,name="logout"),
    path('access/Account/Personal',views.Loginto,name="loginto"),
    path('register',views.Register,name="register")
]