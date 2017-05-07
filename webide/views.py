from django.shortcuts import render, redirect


# Create your views here.
from projects.models import Project


def index(request):
    projects = Project.objects.order_by('-created')[:10]
    # load app
    return render(request, 'index.html', {'projects': projects})
