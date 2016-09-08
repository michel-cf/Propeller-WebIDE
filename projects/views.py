from django.http import JsonResponse
from django.shortcuts import render

from django.views.decorators.http import require_POST, require_GET

# Create your views here.
from projects.models import Project


@require_GET
def create(request):
    return render(request, 'create.html')


@require_POST
def doCreate(request):
    return render(request, 'create.html')
