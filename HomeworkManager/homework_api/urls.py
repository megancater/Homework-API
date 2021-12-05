from django.urls import path
from . import views
from .views import deleteAssignment, createAssignment, updateAssignment, timeAssignment, deleteTimer, timeManagement, timeManagement2

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('timemanagement', views.timeManagement.as_view(), name='timeManagement'),
    path(r'timemanagement2/<month>[A-Za-z]+&<week>[0-9]+', views.timeManagement2.as_view(), name='timeManagement2'),
    path('<id>/delete', deleteAssignment),
    path('<id>/update', updateAssignment),
    path('create', createAssignment),
    path('<int:assignment_id>/',
         views.AssignmentDetailView.as_view(), name='assignment'),
    path('<int:assignment_id>/timer', timeAssignment),
    path('<int:assignment_id>/timer/<id>', deleteTimer)
]
