from django.http.response import HttpResponse
from .models import Project
from django.shortcuts import render


def main_page(request):
    project_objects = Project.objects.all()
    return render(request, 'portfolio/index.html', {'project_objects': project_objects})
