import django_tables2

from projects.models import Project


class MyProjectsTable(django_tables2.Table):

    class Meta:
        sequence = ('name', 'creation_date', 'last_change', 'public')
        exclude = ('id', 'user', 'code', 'git_path')
        template = 'django_tables2/bootstrap.html'
        model = Project


class PublicProjectTable(django_tables2.Table):

    class Meta:
        sequence = ('user', 'name', 'creation_date', 'last_change')
        exclude = ('id', 'code', 'git_path', 'public')
        template = 'django_tables2/bootstrap.html'
        model = Project
