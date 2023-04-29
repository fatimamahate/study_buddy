from django.shortcuts import render, redirect, get_object_or_404
from .models import Assignment
from .forms import AssignmentForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


@login_required
def dashboard(request):
    assignments = Assignment.objects.all()

    context = {
        'assignments': assignments
    }
    return render(request, 'study_app/dashboard.html', context)


@login_required
def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    form = AssignmentForm()
    context = {
        'form': form
    }
    return render(request, 'study_app/add_assignment.html', context)


@login_required
def edit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.user != assignment.tutor:
        return redirect('dashboard')
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    form = AssignmentForm()
    context = {
        'form': form
    }
    return render(request, 'study_app/edit_assignment.html', context)


@login_required
def delete_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.user != assignment.tutor:
        return redirect('dashboard')
    assignment.delete()
    return redirect('dashboard')


def new_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Success!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid information, try again")
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'study_app/sign_up.html', context)
