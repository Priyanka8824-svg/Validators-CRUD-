from django import forms
from django.core import validators
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

    def clean_pid(self):
        p = self.cleaned_data.get('pid')
        if p <= 5:
            raise forms.ValidationError('Please enter valid Pid......')
        return p

    def clean_name(self):
        n = self.cleaned_data.get('name')
        if n.istitle()!=True:
            raise forms.ValidationError("Please enter 1st letter capital.....")
        return n

    def clean_age(self):
        a = self.cleaned_data.get('age')
        if a <= 0:
            raise forms.ValidationError('Please enter valid Age......')
        return a