from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

from .forms import InquiryForm, ProjectForm, RegisterForm, TechStackForm, TestimonyForm
from .models import Inquiry, PersonalInformation, Project, TechStack, Testimony


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


@user_passes_test(lambda user: user.is_active and user.is_superuser, login_url='admin_login')
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            form.save_m2m()
            messages.success(request, 'Project created successfully.')
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'project_create.html', {'form': form})


@user_passes_test(lambda user: user.is_active and user.is_superuser, login_url='admin_login')
def tech_stack_create(request):
    if request.method == 'POST':
        form = TechStackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tech stack created successfully.')
            return redirect('dashboard')
    else:
        form = TechStackForm()
    return render(request, 'tech_stack_create.html', {'form': form})


def admin_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser:
                login(request, user)
                messages.success(request, 'Welcome back, admin.')
                return redirect('dashboard')
        messages.error(request, 'Only administrators can sign in.')
    else:
        form = AuthenticationForm()

    return render(request, 'admin_login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully. Please sign in as the admin.')
            return redirect('admin_login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('admin_login')


@user_passes_test(lambda user: user.is_active and user.is_superuser, login_url='admin_login')
def dashboard(request):
    projects = Project.objects.all().order_by('project_name')
    tech_stacks = TechStack.objects.all().order_by('name')
    return render(request, 'dashboard.html', {'projects': projects, 'tech_stacks': tech_stacks})


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
