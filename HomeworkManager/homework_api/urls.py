from django.urls import path
from . import views
from .views import deleteAssignment, createAssignment, updateAssignment, timeAssignment, deleteTimer, editTimer, loadData, manageTime, timeManagement, timeManagement2, averageManagement

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #path('timemanagement', views.timeManagement.as_view(), name='timeManagement'),
    path('timemanagement', manageTime),  # loadData),
    path('loaddata', loadData, name='load-data'),
    path('averagemanagement', views.averageManagement.as_view(),
         name='averageManagement'),
    path('<id>/delete', deleteAssignment),
    path('<id>/update', updateAssignment),
    path('create', createAssignment),
    path('<int:assignment_id>/',
         views.AssignmentDetailView.as_view(), name='assignment'),
    path('<int:assignment_id>/timer', timeAssignment),
    path('<int:assignment_id>/timer/delete/<id>', deleteTimer),
    path('<int:assignment_id>/timer/edit/<id>', editTimer)
]
