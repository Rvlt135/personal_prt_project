from django.http.response import HttpResponse
from .models import Project
from django.shortcuts import render


def main_page(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/index.html', {'projects': projects})
