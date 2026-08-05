from django.contrib import admin

from .models import Inquiry, PersonalInformation, Project, Testimony


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact_number', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('first_name', 'last_name', 'email', 'message')
    readonly_fields = ('submitted_at',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'tech_stack', 'link')
    search_fields = ('project_name', 'tech_stack')


@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'posted_at')
    search_fields = ('full_name', 'content')
    readonly_fields = ('posted_at',)


@admin.register(PersonalInformation)
class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact_number')
    search_fields = ('first_name', 'last_name', 'email')
