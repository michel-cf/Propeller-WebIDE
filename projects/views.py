from django.http import JsonResponse
from django.shortcuts import render

from django.views.decorators.http import require_POST


# Create your views here.
from projects.models import Project

