
from django.urls import path
from django.contrib import admin
from Base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('emp/',views.emp_register,name='emp_register'),
]