from django.test import TestCase
from workers.models import Position, Worker


class PositionModelTest(TestCase):
    def test_position_creation(self):
        position = Position.objects.create(name="Developer")
        self.assertEqual(position.name, "Developer")
        self.assertEqual(str(position), "Developer")
        self.assertTrue(Position.objects.filter(name="Developer").exists())

    def test_position_unique_name(self):
        Position.objects.create(name="Manager")
        with self.assertRaises(Exception):
            Position.objects.create(name="Manager")


class WorkerModelTest(TestCase):
    def setUp(self):
        self.developer_position = Position.objects.create(name="Developer")
        self.manager_position = Position.objects.create(name="Manager")

        self.worker1 = Worker.objects.create_user(
            username="worker1", first_name="John", last_name="Doe", position=self.developer_position
        )
        self.worker2 = Worker.objects.create_user(
            username="worker2", first_name="Jane", last_name="Smith", position=self.manager_position
        )

    def test_worker_creation(self):
        self.assertEqual(self.worker1.username, "worker1")
        self.assertEqual(self.worker1.position.name, "Developer")
        self.assertEqual(str(self.worker1), "John Doe")

    def test_worker_position_association(self):
        self.assertEqual(self.worker1.position, self.developer_position)
        self.assertEqual(self.worker2.position, self.manager_position)

    def test_worker_unique_username(self):
        with self.assertRaises(Exception):
            Worker.objects.create_user(
                username="worker1", first_name="Alice", last_name="Brown", position=self.developer_position
            )

    def test_worker_str_method(self):
        self.assertEqual(str(self.worker2), "Jane Smith")
