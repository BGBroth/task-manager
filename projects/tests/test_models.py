from django.test import TestCase
from workers.models import Worker
from tasks.models import Tag, TaskType
from projects.models import Team, Project


class TeamProjectModelsTest(TestCase):
    def setUp(self):
        self.worker_1 = Worker.objects.create(username="worker1", first_name="John", last_name="Doe",
                                              password="password")
        self.worker_2 = Worker.objects.create(username="worker2", first_name="Jane", last_name="Doe",
                                              password="password")

        self.tag = Tag.objects.create(name="Urgent")
        self.task_type = TaskType.objects.create(name="Bug")

        self.team = Team.objects.create(name="Development Team")
        self.team.members.add(self.worker_1, self.worker_2)

        self.project = Project.objects.create(name="Project A", description="A description for Project A")
        self.project.teams.add(self.team)

    def test_team_creation(self):
        self.assertEqual(self.team.name, "Development Team")
        self.assertEqual(self.team.members.count(), 2)
        self.assertIn(self.worker_1, self.team.members.all())
        self.assertIn(self.worker_2, self.team.members.all())

    def test_project_creation(self):
        self.assertEqual(self.project.name, "Project A")
        self.assertEqual(self.project.description, "A description for Project A")
        self.assertEqual(self.project.teams.count(), 1)
        self.assertIn(self.team, self.project.teams.all())

    def test_team_str_method(self):
        self.assertEqual(str(self.team), "Development Team")

    def test_project_str_method(self):
        self.assertEqual(str(self.project), "Project A")

    def test_project_and_team_relationship(self):
        self.assertIn(self.team, self.project.teams.all())
        self.assertIn(self.project, self.team.projects.all())
