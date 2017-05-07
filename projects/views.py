import logging
from raven.contrib.django.raven_compat.models import client
import os

from django.conf import settings
from django.http import HttpResponseRedirect
from django.http import HttpResponseServerError
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.http import require_POST, require_GET

from projects.forms import CreateProjectForm
from projects.models import Project, Branch

# Create your views here.


logger = logging.getLogger(__name__)


def create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateProjectForm(request.user, request.POST)
        # check whether it's valid:
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user

            project.save()

            # Create master branch
            branch = Branch()
            branch.project = project
            branch.code = 'master'
            branch.name = 'master'

            branch.save()

            return redirect('projects:project', project.user.username, project.code)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateProjectForm(request.user)

    logger.error("Project already exists")
    return render(request, 'create.html', {'form': form})


def editor(request, username, projectcode):
    project = get_object_or_404(Project, user__username=username, code=projectcode)
    return render(request, 'editor.html', {
        'project': project
    })
