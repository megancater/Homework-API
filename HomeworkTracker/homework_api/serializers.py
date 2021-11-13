from .models import Assignment, Timer
from rest_framework import serializers

class AssignmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'name', 'due_date', 'class_name', 'description', 'status']

class TimerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Timer
        fields = ['id', 'assignment', 'begin', 'end']
