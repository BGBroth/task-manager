from django.test import TestCase
from django.utils import timezone
from projects.models import Project
from tasks.models import TaskType, Tag, Task


class TaskTypeModelTest(TestCase):
    def test_task_type_creation(self):
        task_type = TaskType.objects.create(name="Bug")
        self.assertEqual(task_type.name, "Bug")
        self.assertEqual(str(task_type), "Bug")
        self.assertTrue(TaskType.objects.filter(name="Bug").exists())

    def test_task_type_unique_name(self):
        TaskType.objects.create(name="Feature")
        with self.assertRaises(Exception):
            TaskType.objects.create(name="Feature")


class TagModelTest(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(name="Urgent")
        self.assertEqual(tag.name, "Urgent")
        self.assertEqual(str(tag), "Urgent")
        self.assertTrue(Tag.objects.filter(name="Urgent").exists())

    def test_tag_unique_name(self):
        Tag.objects.create(name="Backend")
        with self.assertRaises(Exception):
            Tag.objects.create(name="Backend")


class TaskModelTest(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="Bug")
        self.project = Project.objects.create(name="Project A")
        self.tag = Tag.objects.create(name="Urgent")

    def test_task_creation(self):
        task = Task.objects.create(
            name="Fix login issue",
            description="The login page throws an error when submitting.",
            deadline=timezone.now().date(),
            priority="High",
            task_type=self.task_type,
            project=self.project,
        )
        self.assertEqual(task.name, "Fix login issue")
        self.assertEqual(task.priority, "High")
        self.assertEqual(task.task_type, self.task_type)
        self.assertEqual(task.project, self.project)
        self.assertFalse(task.is_completed)
        self.assertTrue(Task.objects.filter(name="Fix login issue").exists())

    def test_task_with_tags(self):
        task = Task.objects.create(
            name="Implement feature X",
            description="Feature X should be implemented.",
            deadline=timezone.now().date(),
            priority="Medium",
            task_type=self.task_type,
            project=self.project,
        )
        task.tags.add(self.tag)
        self.assertIn(self.tag, task.tags.all())

    def test_task_is_completed_default(self):
        task = Task.objects.create(
            name="Task with default completion",
            description="This task has a default is_completed value.",
            deadline=timezone.now().date(),
            priority="Medium",
            task_type=self.task_type,
            project=self.project,
        )
        self.assertFalse(task.is_completed)

    def test_task_str_method(self):
        task = Task.objects.create(
            name="Test Task",
            description="This is a test task.",
            deadline=timezone.now().date(),
            priority="Medium",
            task_type=self.task_type,
            project=self.project,
        )
        self.assertEqual(str(task), "Test Task")
