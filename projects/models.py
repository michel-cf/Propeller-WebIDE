from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, related_name='projects')
    code = models.SlugField()
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_created=True)
    last_change = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=False)

    class Meta:
        unique_together = (('user', 'code'),)


class Branch(models.Model):
    project = models.ForeignKey(Project, related_name='branches')
    code = models.SlugField()
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = (('project', 'name'),)


class File(models.Model):
    previous = models.ForeignKey('File', related_name='new_file_revisions', null=True)
    path = models.CharField(max_length=1000)
    filename = models.CharField(max_length=255)
    file = models.TextField()
    mime = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)


class Revision(models.Model):
    branch = models.ForeignKey(Branch, related_name='revisions')
    previous = models.ForeignKey('Revision', related_name='new_revisions', null=True)
    files = models.ManyToManyField(File, related_name='revisions')
    comment = models.TextField(null=True)
    committed = models.BooleanField(default=False)
    committed_at = models.DateTimeField(null=True)
