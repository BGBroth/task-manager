from django.contrib.auth.models import AbstractUser
from django.db import models

from tasks.models import Task


class Position(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "task_manager_position"

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position, on_delete=models.SET_NULL, null=True, related_name="workers"
    )

    def get_all_tasks(self):
        return Task.objects.filter(project__teams__members=self).distinct()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
