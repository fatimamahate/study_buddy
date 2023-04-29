from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Assignment(models.Model):
    title = models.CharField(max_length=75, null=False, blank=False)
    tutor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='created_assignments')
    tutee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='assignments_todo')
    content = models.TextField()

def __str__(self):
    return self.title
    
