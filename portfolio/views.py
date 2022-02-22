# Python packages
from datetime import date
from django.contrib.admin.views.decorators import staff_member_required

# Imports for Django views
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Imports for django forms
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Django authentication and messaging features
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import *
from .models import *

# Create your views here.


def homepage(request):
    projects = Project.objects.all()

    context = {
        'projects': projects,
    }

    template_name = '../templates/base.html'

    return render(request, template_name, context)


def portfolio(request):
    list(messages.get_messages(request))
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Project saved")
            return redirect('portfolio')
        else:
            print("Project didn't save")
            messages.error(request, "Project didn't save")

    projects = Project.objects.all()

    context = {
        'projects': projects,
        'form': form,
    }

    template_name = '../templates/portfolio.html'

    return render(request, template_name, context)
