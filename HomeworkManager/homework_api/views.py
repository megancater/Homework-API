from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Assignment, Timer
from .forms import AssignmentForm, TimerForm

class IndexView(ListView):
    template_name = 'homework_api/index.html'
    context_object_name = 'assignment_list'

    def get_queryset(self):
        return Assignment.objects.order_by('due_date')

class AssignmentDetailView(ListView):
    model = Assignment
    template_name = 'homework_api/index.html'

def updateAssignment(request, id):
    context = {}
    obj = get_object_or_404(Assignment, id = id)
    form = AssignmentForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    context['form'] = form
    return render(request, 'updateAssignment.html', context)


def deleteAssignment(request, id):
    context = {}
    assignment = get_object_or_404(Assignment, id=id)
    if request.method == "POST":
        assignment.delete()
        return HttpResponseRedirect("/")
    return render(request, "deleteAssignment.html", context)

def createAssignment(request):
    context = {}

    form = AssignmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    context['form'] = form
    return render(request, "createAssignment.html", context)

