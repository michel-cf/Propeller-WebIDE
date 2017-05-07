import logging

from django_tables2 import RequestConfig
from raven.contrib.django.raven_compat.models import client
import os

from django.conf import settings
from django.http import HttpResponseRedirect
from django.http import HttpResponseServerError
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.http import require_POST, require_GET

from projects.forms import CreateProjectForm
from projects.models import Project
from projects.tables import MyProjectsTable, PublicProjectTable

logger = logging.getLogger(__name__)


def license_page(request):
    return render(request, 'license.html')


def changelog_page(request):
    return render(request, 'changelog.html')


def libraries_page(request):
    return render(request, 'libraries.html')


def communicator_download(request):
    return render(request, 'communicator-download.html')
