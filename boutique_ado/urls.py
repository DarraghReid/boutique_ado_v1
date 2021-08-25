"""boutique_ado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Create a path called accounts, use it to include all
    # allauth urls
    # Gives us all the urls for login/logout, password resets etc
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    # Include prodcuts.urls urls in thid project level file
    # Give them a top level URL of products/
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
