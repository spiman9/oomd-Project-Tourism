from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
      path("",views.home,name="home"),
      path("india",views.india,name="bookIndia"),
      path("dubai",views.dubai,name="bookDubai"),
      path("singapore",views.singapore,name="bookSingapore"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)