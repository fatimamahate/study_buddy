from django.shortcuts import render, redirect, get_object_or_404
from .models import Assignment
from .forms import AssignmentForm
from django.contrib.auth.models import User

# Create your views here.


def dashboard(request):
    assignments = Assignment.objects.all()
    
    context = {
        'assignments': assignments
    }
    return render(request, 'study_app/dashboard.html', context)


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
