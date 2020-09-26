from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('RegisterAsUser',views.RegisterAsUser,name = "RegisterAsUser"),
    path('RegisterAsNgo',views.RegisterAsNgo,name = "RegisterAsNgo"),
    path('LoginAsNgo',views.LoginAsNgo,name = "LoginAsNgo"),
    path('LoginAsUser',views.LoginAsUser,name="LoginAsUser"),
]
