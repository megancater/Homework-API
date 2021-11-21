from django import forms
from .models import Assignment

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = [
            'name',
            'due_date',
            'class_name',
            'description',
            'completed'
        ]
