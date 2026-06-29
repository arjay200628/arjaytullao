from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about_me(request):
    return render(request, 'about me.html')


def projects(request):
    return render(request, 'my projects.html')


def contacts(request):
    return render(request, 'contacts.html')
