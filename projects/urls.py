from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.projects, name='list'),  # Changed from 'projects' to 'list'
    path('<int:project_id>/', views.project_detail, name='detail'),  # Add detail view URL
]
