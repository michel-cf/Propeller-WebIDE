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


def create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateProjectForm(request.user, request.POST)
        # check whether it's valid:
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user

            # Create GIT repository
            project_directory = os.path.join(settings.WEBIDE_GIT_ROOT, project.user.username, project.code)
            if not os.path.exists(project_directory):
                try:
                    # Create repo location
                    os.makedirs(project_directory)

                    # Create repo
                    git_repo = Repo.init(project_directory)

                    project.git_path = project_directory
                    project.save()

                    return redirect('projects:project', project.user.username, project.code)
                except OSError as ose:
                    client.captureException()
                    logger.error("Could not create project git directory", ose)
            else:
                logger.error("Could not create project git directory, directory already exists")

            return HttpResponseServerError()
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


def community(request):
    queryset = Project.objects.filter(public=True)
    table = PublicProjectTable(queryset)
    RequestConfig(request, paginate={'per_page': 25}).configure(table)
    return render(request, 'community.html', {'table': table})


def my_projects(request):
    queryset = Project.objects.filter(user=request.user)
    table = MyProjectsTable(queryset)
    RequestConfig(request, paginate={'per_page': 25}).configure(table)
    return render(request, 'my_projects.html', {'table': table})
