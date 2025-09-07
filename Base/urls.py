from django.urls import path
from Base import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('emp/',views.emp_register,name='emp_register'),
]