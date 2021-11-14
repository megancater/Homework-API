from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Assignment, Timer

class IndexView(ListView):
    template_name = 'homework_api/index.html'
    context_object_name = 'assignment_list'

    def get_queryset(self):
        return Assignment.objects.order_by('due_date')

class AssignmentDetailView(ListView):
    model = Assignment
    template_name = 'homework_api/index.html'

def complete(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)

