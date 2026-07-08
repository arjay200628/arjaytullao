from django.shortcuts import get_object_or_404, render

from .models import PersonalInformation, Project


def home(request):
    personal_info = PersonalInformation.objects.first()
    return render(request, 'home.html', {'personal_info': personal_info})


def about_me(request):
    personal_info = PersonalInformation.objects.first()
    return render(request, 'about me.html', {'personal_info': personal_info})


def personal_information(request):
    personal_info = PersonalInformation.objects.first()
    return render(request, 'personal information.html', {'personal_info': personal_info})


def project_list(request):
    projects = Project.objects.all().order_by('project_name')
    return render(request, 'my projects.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})


def contacts(request):
    personal_info = PersonalInformation.objects.first()
    return render(request, 'contacts.html', {'personal_info': personal_info})
