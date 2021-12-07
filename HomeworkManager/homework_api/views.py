from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import ListView, DetailView
from django.db.models import Q, OuterRef, Subquery
from .models import Assignment, Timer
from .forms import AssignmentForm, TimerForm
#import json


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
    obj = get_object_or_404(Assignment, id=id)
    form = AssignmentForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    context['form'] = form
    return render(request, 'updateAssignment.html', context)


def deleteAssignment(request, id):
    context = {}
    assignment = get_object_or_404(Assignment, id=id)
    if request.method == 'POST':
        assignment.delete()
        return HttpResponseRedirect('/')
    return render(request, 'deleteAssignment.html', context)


def createAssignment(request):
    context = {}

    form = AssignmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    context['form'] = form
    return render(request, 'createAssignment.html', context)


def timeAssignment(request, assignment_id):
    context = {}
    assignment = get_object_or_404(Assignment, id=assignment_id)

    if request.method == 'POST':
        if 'create_timer' in request.POST:
            timer = Timer.objects.create(assignment=assignment)
            timer.save()
            return render(request, 'timeAssignment.html', context)
        if 'stop_timer' in request.POST:
            timerList = assignment.timers.all()
            print(timerList)
            timerList[len(timerList)-1].save()
            return HttpResponseRedirect('/')

    return render(request, 'timeAssignment.html', context)


def deleteTimer(request, assignment_id, id):
    context = {}
    assignment = get_object_or_404(Assignment, id=assignment_id)

    if 'delete_timer' in request.POST:
        timer = assignment.timers.filter(id=id)
        timer.delete()
        return HttpResponseRedirect('/')

    return render(request, 'deleteTimer.html', context)


def editTimer(request, assignment_id, id):
    context = {}
    assignment = get_object_or_404(Assignment, id=assignment_id)
    timer = assignment.timers.filter(id=id).first()

    form = TimerForm(request.POST or None, instance=timer)
    if form.is_valid():
        updatedTimer = form.save(commit=False)
        updatedTimer.edit()
        return HttpResponseRedirect('/')

    context['form'] = form
    return render(request, 'editTimer.html', context)


def manageTime(request):
    return render(request, 'timeManagement2.html')


def loadData(request):
    data = Assignment.objects.all()
    processedData = list(Assignment.objects.values(
        'name', 'due_date', 'class_name', 'description', 'completed'))

    for i, assign in enumerate(data):
        timersList = []
        for timer in assign.timers.all():
            timersList.append({
                'id': timer.id,
                'begin': timer.begin,
                'end': timer.end
            })
        processedData[i]['timers'] = timersList

    return JsonResponse(processedData, safe=False)


class timeManagement(ListView):
    template_name = 'timeManagement.html'
    context_object_name = 'assignment_list'

    def get_queryset(self):
        return Assignment.objects.order_by('due_date')


class timeManagement2(ListView):
    template_name = 'timeManagement2.html'
    context_object_name = 'assignment_list'

    def get_queryset(self):
        return Assignment.objects.order_by('due_date')


class averageManagement(ListView):
    template_name = 'averageManagement.html'
    context_object_name = 'assignment_list'

    def get_queryset(self):
        return Assignment.objects.order_by('due_date')
