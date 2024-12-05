from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import TagSearchForm, TaskTypeSearchForm, TaskSearchForm
from tasks.models import Task, TaskType, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5
    queryset = Task.objects.select_related("task_type")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["search_form"] = TaskSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            return Task.objects.filter(name__icontains=name)
        return Task.objects.all()


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


class TaskTypeListView(generic.ListView):
    model = TaskType
    paginate_by = 5
    context_object_name = 'task_type_list'
    template_name = "tasks/task_type_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["search_form"] = TaskTypeSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            return TaskType.objects.filter(name__icontains=name)
        return TaskType.objects.all()


class TaskTypeDetailView(generic.DetailView):
    model = TaskType
    context_object_name = 'task_type'
    template_name = "tasks/task_type_detail.html"


class TaskTypeCreateView(generic.CreateView):
    model = TaskType
    fields = "__all__"
    template_name = "tasks/task_type_form.html"
    success_url = reverse_lazy("tasks:task-type-list")


class TaskTypeUpdateView(generic.UpdateView):
    model = TaskType
    fields = "__all__"
    template_name = "tasks/task_type_form.html"
    success_url = reverse_lazy("tasks:task-type-list")


class TaskTypeDeleteView(generic.DeleteView):
    model = TaskType
    context_object_name = 'task_type'
    template_name = "tasks/task_type_confirm_delete.html"
    success_url = reverse_lazy("tasks:task-type-list")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5
    queryset = Tag.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["search_form"] = TagSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            return Tag.objects.filter(name__icontains=name)
        return Tag.objects.all()


class TagDetailView(generic.DetailView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
