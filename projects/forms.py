from django import forms
from django.core.exceptions import ValidationError

from projects.models import Project


class CreateProjectForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(CreateProjectForm, self).__init__(*args, **kwargs)

    def clean_name(self):
        return self.cleaned_data['name'].strip()

    def clean_code(self):
        code = self.cleaned_data['code'].strip().lower().replace(' ', '_')
        if Project.objects.filter(user=self.user, code=code).exists():
            raise ValidationError('A project with this code already exists')
        return code

    class Meta:
        model = Project
        fields = ['name', 'code', 'public']


class CreateProjectFormBasic(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    code = forms.SlugField(label='Code', max_length=255)

    def clean_name(self):
        return self.cleaned_data['name'].strip()

    def clean_code(self):
        return self.cleaned_data['code'].strip().lower().replace(' ', '_')
