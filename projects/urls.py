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

app_name = 'projects'
urlpatterns = [
    url(r'^create.html$', views.create, name='create'),
    url(r'^(?P<username>[\w-]+)/(?P<project_code>[\w-]+)$', views.editor, name='project'),
    url(r'^public.html$', views.community, name='community'),
    url(r'^myprojects.html$', views.my_projects, name='my_projects'),
]
