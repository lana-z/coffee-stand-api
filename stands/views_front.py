from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Stand


class StandListView(LoginRequiredMixin, ListView):
    template_name = "stands/stand_list.html"
    model = Stand
    context_object_name = "stands"


class StandDetailView(LoginRequiredMixin, DetailView):
    template_name = "stands/stand_detail.html"
    model = Stand


class StandUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "stands/stand_update.html"
    model = Stand
    fields = "__all__"


class StandCreateView(LoginRequiredMixin, CreateView):
    template_name = "stands/stand_create.html"
    model = Stand
    fields = ["name", "rating", "reviewer"] # "__all__" for all of them


class StandDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "stands/stand_delete.html"
    model = Stand
    success_url = reverse_lazy("stand_list")
