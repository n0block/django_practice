from django.forms import ModelForm
from .models import Dashboard


class CrewMemberForm(ModelForm):
    class Meta:
        model = Dashboard
        fields = ['first_name', 'second_name', 'crew']

