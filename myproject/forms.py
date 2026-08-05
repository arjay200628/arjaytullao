from django import forms

from .models import Inquiry, Project, Testimony


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'description', 'tech_stack', 'link']
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Project name'}),
            'description': forms.Textarea(attrs={'class': 'input-field', 'rows': 5, 'placeholder': 'Project description'}),
            'tech_stack': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Tech stack'}),
            'link': forms.URLInput(attrs={'class': 'input-field', 'placeholder': 'Project link'}),
        }


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['first_name', 'last_name', 'contact_number', 'email', 'address', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Last name'}),
            'contact_number': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Contact number'}),
            'email': forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Email address'}),
            'address': forms.Textarea(attrs={'class': 'input-field', 'rows': 3, 'placeholder': 'Address'}),
            'message': forms.Textarea(attrs={'class': 'input-field', 'rows': 5, 'placeholder': 'Your message'}),
        }


class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ['full_name', 'content']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Your full name'}),
            'content': forms.Textarea(attrs={'class': 'input-field', 'rows': 5, 'placeholder': 'Write your testimony'}),
        }
