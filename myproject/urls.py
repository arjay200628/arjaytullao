"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about-me/', views.about_me, name='about_me'),
    path('personal-information/', views.personal_information, name='personal_information'),
    path('my-projects/', views.project_list, name='projects'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/project/create/', views.project_create, name='project_create'),
    path('dashboard/tech-stack/create/', views.tech_stack_create, name='tech_stack_create'),
    path('contacts/', views.contact_inquiry, name='contacts'),
    path('testimonials/', views.TestimonyListView.as_view(), name='testimonials'),
    path('testimony/<int:pk>/', views.testimony_detail, name='testimony_detail'),
    path('leave-testimony/', views.testimony_create, name='testimony_create'),
]
