from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import ListView, DetailView
from django.db.models import Q, OuterRef, Subquery
from .models import Assignment, Timer
from .forms import AssignmentForm, TimerForm

# List of assignments
class IndexView(ListView):
    template_name = 'homework_api/index.html'
    context_object_name = 'assignment_list'

    # Returns assignments list
    def get_queryset(self):
        return Assignment.objects.order_by('due_date')

# During execution, contains the current assignment being operated on
class AssignmentDetailView(ListView):
    model = Assignment
    template_name = 'homework_api/index.html'

# Updates assignment details
def updateAssignment(request, id):
    context = {}

    # Gets assignment
    obj = get_object_or_404(Assignment, id=id)

    # Creates assignment form
    form = AssignmentForm(request.POST or None, instance=obj)

    # Saves form data
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    context['form'] = form
    return render(request, 'updateAssignment.html', context)

# Deletes assignment
def deleteAssignment(request, id):
    context = {}

    # Gets assignment
    assignment = get_object_or_404(Assignment, id=id)

    # Deletes the assignment
    if request.method == 'POST':
        assignment.delete()
        return HttpResponseRedirect('/')

    return render(request, 'deleteAssignment.html', context)

# Creates a new assignment
def createAssignment(request):
    context = {}

    # Creates assignment form
    form = AssignmentForm(request.POST or None)

    # Saves form data
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    context['form'] = form
    return render(request, 'createAssignment.html', context)

# Creates timer with begin and end
def timeAssignment(request, assignment_id):
    context = {}

    # Gets assignment
    assignment = get_object_or_404(Assignment, id=assignment_id)

    if request.method == 'POST':
        # Creates timer if timer is started
        if 'create_timer' in request.POST:
            timer = Timer.objects.create(assignment=assignment)
            timer.save()
            return render(request, 'timeAssignment.html', context)

        # Updates and saves timer with end time
        if 'stop_timer' in request.POST:
            timerList = assignment.timers.all()
            print(timerList)
            timerList[len(timerList)-1].save()
            return HttpResponseRedirect('/')

    return render(request, 'timeAssignment.html', context)

# Deletes timer
def deleteTimer(request, assignment_id, id):
    context = {}

    # Gets assignment associated with timer
    assignment = get_object_or_404(Assignment, id=assignment_id)

    # Deletes timer
    if 'delete_timer' in request.POST:
        timer = assignment.timers.filter(id=id)
        timer.delete()
        return HttpResponseRedirect('/')

    return render(request, 'deleteTimer.html', context)

# Updates timer details
def editTimer(request, assignment_id, id):
    context = {}

    # Gets assignment associated with timer
    assignment = get_object_or_404(Assignment, id=assignment_id)

    # Gets timer
    timer = assignment.timers.filter(id=id).first()

    # Creates form for updating timer
    form = TimerForm(request.POST or None, instance=timer)

    # Updates and saves timer details
    if form.is_valid():
        updatedTimer = form.save(commit=False)
        updatedTimer.edit()
        return HttpResponseRedirect('/')

    context['form'] = form
    return render(request, 'editTimer.html', context)

# Time management requests
def manageTime(request):
    return render(request, 'timeManagement2.html')

# Average time management requests
def manageAverage(request):
    return render(request, 'averageManagement2.html')

# Loads assignment and timer data
def loadData(request):
    # Gets all assignments and processes as list
    data = Assignment.objects.all()
    processedData = list(Assignment.objects.values(
        'name', 'due_date', 'class_name', 'description', 'completed'))

    # For each assignment creates a list of associated timers
    for i, assign in enumerate(data):
        timersList = []

        # Adds timer data as dictionary to list
        for timer in assign.timers.all():
            timersList.append({
                'id': timer.id,
                'begin': timer.begin,
                'end': timer.end
            })

        # Adds timer list to assignment
        processedData[i]['timers'] = timersList

    return JsonResponse(processedData, safe=False)

