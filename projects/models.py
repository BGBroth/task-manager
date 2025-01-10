from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField('workers.Worker', related_name="teams")

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    teams = models.ManyToManyField(Team, related_name="projects")

    def __str__(self):
        return self.name