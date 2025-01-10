from django.db import models
from projects.models import Project

class TaskType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "task_manager_task_type"

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Urgent', 'Urgent'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    task_type = models.ForeignKey(
        TaskType, on_delete=models.SET_NULL, null=True, related_name="tasks"
    )
    project = models.ForeignKey(
        Project, on_delete=models.SET_NULL, null=True, related_name="tasks"
    )
    tags = models.ManyToManyField(Tag, related_name="tasks", blank=True)

    def __str__(self):
        return self.name