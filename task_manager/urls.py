from django.urls import path

from task_manager.views import index, WorkerListView, TaskListView, TaskTypeListView, PositionListView

urlpatterns = [
    path("", index, name="index"),
    path(
        "workers/",
        WorkerListView.as_view(),
        name="worker-list",
    ),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list",
    ),
    path(
        "task-types/",
        TaskTypeListView.as_view(),
        name="task-type-list",
    ),
    path(
        "positions/",
        PositionListView.as_view(),
        name="position-list",
    ),
]

app_name = "task_manager"
