"""taggy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.utils.translation import ugettext_lazy

import views

app_name = 'webide'
urlpatterns = [
    # Plugins
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),

    # Index
    url(r'^$', views.index),
    url(r'^index.html$', views.index, name='index'),

    # Apps
    url(r'^project/', include('projects.urls')),
]


admin.site.site_header = ugettext_lazy('Propeller WebIDE admin')
admin.site.site_title = ugettext_lazy('Propeller WebIDE administration')