from django import forms
from .models import Assignment, Timer


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


class TimerForm(forms.ModelForm):
    class Meta:
        model = Timer
        fields = [
            'begin',
            'end'
        ]
