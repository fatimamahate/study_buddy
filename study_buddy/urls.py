"""study_buddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from study_app.views import dashboard, edit_assignment, add_assignment, delete_assignment, new_user, current_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard', dashboard, name='dashboard'),
    path('assignment_add', add_assignment, name='add'),
    path('assignment_edit/<assignment_id>', edit_assignment, name='edit'),
    path('assignment_delete/<assignment_id>', delete_assignment, name='delete'),
    path('sign_up', new_user, name='register'),
    path('', current_user, name='login')
]
