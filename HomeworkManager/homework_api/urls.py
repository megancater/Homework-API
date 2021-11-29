from django.urls import path
from . import views
from .views import deleteAssignment, createAssignment, updateAssignment, timeAssignment

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<id>/delete', deleteAssignment),
    path('<id>/update', updateAssignment),
    path('create', createAssignment),
    path('<int:assignment_id>/', views.AssignmentDetailView.as_view(), name='assignment')
]
