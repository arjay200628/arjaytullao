from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Inquiry, Project, TechStack, Testimony


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input-field'})


class ProjectForm(forms.ModelForm):
    tech_stacks = forms.ModelMultipleChoiceField(
        queryset=TechStack.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta:
        model = Project
        fields = ['project_name', 'description', 'tech_stacks', 'link']
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Project name'}),
            'description': forms.Textarea(attrs={'class': 'input-field', 'rows': 5, 'placeholder': 'Project description'}),
            'link': forms.URLInput(attrs={'class': 'input-field', 'placeholder': 'Project link'}),
        }


class TechStackForm(forms.ModelForm):
    class Meta:
        model = TechStack
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Tech stack name'}),
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
