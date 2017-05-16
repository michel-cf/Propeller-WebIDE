import django_tables2

from projects.models import Project


class MyProjectsTable(django_tables2.Table):
    name = django_tables2.LinkColumn('projects:project',
                                     args=[django_tables2.A('user.username'), django_tables2.A('name')])

    class Meta:
        sequence = ('name', 'created', 'last_change', 'public')
        exclude = ('id', 'user', 'code')
        template = 'django_tables2/bootstrap.html'
        model = Project


class PublicProjectTable(django_tables2.Table):
    name = django_tables2.LinkColumn('projects:project',
                                     args=[django_tables2.A('user.username'), django_tables2.A('name')])

    class Meta:
        sequence = ('user', 'name', 'created', 'last_change')
        exclude = ('id', 'code', 'public')
        template = 'django_tables2/bootstrap.html'
        model = Project
