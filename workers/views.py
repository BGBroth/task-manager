from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from workers.forms import PositionSearchForm, WorkerSearchForm, WorkerCreationForm
from workers.models import Position, Worker


class PositionListView(LoginRequiredMixin, generic.ListView):
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


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("workers:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("workers:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("workers:position-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
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
        username = self.request.GET.get("username")
        if username:
            return Worker.objects.filter(username__icontains=username)
        return Worker.objects.all()


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("workers:worker-list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("workers:worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("workers:worker-list")
