"""clinico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from appbase.views import InicioView
from appbase.login import *
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginFormView.as_view(), name='login'),
    path('logout/', logout_user),
    path('base/', InicioView.as_view(), name='inicio'),
    path('base/', include('appbase.urls')),
    path('atencion/', include('appconsulta.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
