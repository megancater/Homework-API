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



from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class AssignmentList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'assignment_list.html'

    def get(self, request):
        queryset = Assignment.objects.all()
        return Response({'assignments': queryset})

