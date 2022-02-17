from django.urls import path,include
from . import views


app_name ="user"

urlpatterns = [
    
    path('',views.home,name='home'),
   
    # path('loginpage',views.login,name='loginpage'),

    # path('signup',views.signup,name='signup'),

   
]