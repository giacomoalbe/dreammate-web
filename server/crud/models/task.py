from django.db import models
from .project import Project

class Task(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=1000, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
