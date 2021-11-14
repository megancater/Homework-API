from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:assignment_id>/', views.AssignmentDetailView.as_view(), name='assignment')
]
