from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, related_name='projects')
    code = models.SlugField(max_length=255)
    name = models.CharField(max_length=255)
    git_path = models.CharField(max_length=2000)
    public = models.BooleanField(default=False)
    creation_date = models.DateTimeField()
    last_change = models.DateTimeField()

    class Meta:
        unique_together = (('user', 'code'),)
        ordering = ('-last_change',)
