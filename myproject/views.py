from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

from .forms import InquiryForm, ProjectForm, TestimonyForm
from .models import Inquiry, PersonalInformation, Project, Testimony


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


def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'project_create.html', {'form': form})


def contact_inquiry(request):
    personal_info = PersonalInformation.objects.first()
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts')
    else:
        form = InquiryForm()
    return render(request, 'contacts.html', {
        'personal_info': personal_info,
        'form': form,
    })


def testimony_create(request):
    if request.method == 'POST':
        form = TestimonyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonials')
    else:
        form = TestimonyForm()
    return render(request, 'testimony_form.html', {'form': form})


class TestimonyListView(ListView):
    model = Testimony
    template_name = 'testimonials.html'
    context_object_name = 'testimonies'
    ordering = ['-posted_at']


def testimony_detail(request, pk):
    testimony = get_object_or_404(Testimony, pk=pk)
    return render(request, 'testimony_detail.html', {'testimony': testimony})
