from django.shortcuts import render, get_object_or_404
from .models import Project

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/home.html')  # Update template name

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {'project': project}
    return render(request, 'projects/detail.html', context)
