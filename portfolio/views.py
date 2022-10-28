from django.shortcuts import render
from .models import Project, Profile


def home(request):
    project_web = Project.objects.filter(type_proyect=1).order_by("date")
    project_app = Project.objects.filter(type_proyect=2).order_by("date")
    profile = Profile.objects.first()
    return render(request, 'home.html', {'project_web': project_web, 'project_app': project_app, 'profile': profile })
