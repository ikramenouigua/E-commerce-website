from django.forms import ModelForm
from .models import person

class FormPerson(ModelForm):
    class Meta:
        model=person
        fields= '__all__'

