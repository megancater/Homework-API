from django.shortcuts import render
from .models import Assignment, Timer
from rest_framework import viewsets
from .serializers import AssignmentSerializer, TimerSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all().order_by('due_date')
    serializer_class = AssignmentSerializer

class TimerViewSet(viewsets.ModelViewSet):
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer
