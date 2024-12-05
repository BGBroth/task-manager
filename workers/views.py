from django.views import generic
from django.urls import reverse_lazy

from workers.forms import PositionSearchForm, WorkerSearchForm, WorkerCreationForm
from workers.models import Position, Worker


class PositionListView(generic.ListView):
    model = Position
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PositionListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["search_form"] = PositionSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            return Position.objects.filter(name__icontains=name)
        return Position.objects.all()


class PositionDetailView(generic.DetailView):
    model = Position


class PositionCreateView(generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("workers:position-list")


class PositionUpdateView(generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("workers:position-list")


class PositionDeleteView(generic.DeleteView):
    model = Position
    success_url = reverse_lazy("workers:position-list")


class WorkerListView(generic.ListView):
    model = Worker
    paginate_by = 5
    queryset = Worker.objects.select_related("position")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["search_form"] = WorkerSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            return Worker.objects.filter(name__icontains=name)
        return Worker.objects.all()


class WorkerDetailView(generic.DetailView):
    model = Worker


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("workers:worker-list")


class WorkerUpdateView(generic.UpdateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("workers:worker-list")


class WorkerDeleteView(generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("workers:worker-list")
