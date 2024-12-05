from django.urls import reverse_lazy
from django.views import generic

from projects.forms import ProjectSearchForm, TeamSearchForm
from projects.models import Project, Team


class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["search_form"] = ProjectSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            return Project.objects.filter(name__icontains=name)
        return Project.objects.all()


class ProjectDetailView(generic.DetailView):
    model = Project


class ProjectCreateView(generic.CreateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("projects:project-list")


class ProjectUpdateView(generic.UpdateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("projects:project-list")


class ProjectDeleteView(generic.DeleteView):
    model = Project
    success_url = reverse_lazy("projects:project-list")


class TeamListView(generic.ListView):
    model = Team
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TeamListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["search_form"] = TeamSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            return Team.objects.filter(name__icontains=name)
        return Team.objects.all()


class TeamDetailView(generic.DetailView):
    model = Team


class TeamCreateView(generic.CreateView):
    model = Team
    fields = "__all__"
    success_url = reverse_lazy("projects:team-list")


class TeamUpdateView(generic.UpdateView):
    model = Team
    fields = "__all__"
    success_url = reverse_lazy("projects:team-list")


class TeamDeleteView(generic.DeleteView):
    model = Team
    success_url = reverse_lazy("projects:team-list")
