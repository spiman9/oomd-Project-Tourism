from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
      path("",views.home,name="home"),
      path("contactus",views.contactus,name="contactus"),
      path("back",views.home,name="back"),
      path("contactussub",views.contactussub,name="contactussub"),
      path("register", views.register,name="register"),
      path("login", views.login,name="login"),
      path("fillregister",views.fillregister,name="fillregister"),
      path("logout", views.logout,name="logout"),
      path("filllogin", views.filllogin,name="filllogin"),
]