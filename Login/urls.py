from django.urls import path
from . import views
from .views import EmailValidationView
from django.views.decorators.csrf import csrf_exempt
urlpatterns=[
    path('',views.Login,name="login"),
    path('Account/Logout',views.Logout,name="logout"),
    path('access/Account/Personal',views.Loginto,name="loginto"),
    path('register',views.Register,name="register"),
    path('email-validate',csrf_exempt(EmailValidationView.as_view()),name="validate-email")
]