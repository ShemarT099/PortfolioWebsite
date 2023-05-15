from django.shortcuts import render
from website.models import Project


def website(request):
    return render(request, 'Website.html', {})

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects' : projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

def blog_index(request):
    return render(request, 'blog_index.html', context)