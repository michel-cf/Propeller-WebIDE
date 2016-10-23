from django.shortcuts import render, redirect


# Create your views here.
from projects.models import Project


def index(request):
    # load app
    projects = Project.objects.filter(public=True)[0:5]
    return render(request, 'index.html', {'projects':projects})
