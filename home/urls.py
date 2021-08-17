from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Create a path called accounts, use it to include all
    # allauth urls
    # Gives us all the urls for login/logout, password resets etc
    path('', views.index, name="home"),
]
