from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Mission
from django.contrib import messages

# Create your views here.


class HomePage(generic.ListView):
    queryset = Mission.objects.filter(approved=True).order_by('-date')[:3]
    template_name = "reports/home_page.html"


class MissionsPage(generic.ListView):
    queryset = Mission.objects.filter(approved=True).order_by('-date')
    paginate_by = 2
    model = Mission
    template_name = "reports/missions_page.html"


class MyReportsPage(generic.ListView):
    model = Mission
    template_name = "reports/my_reports_page.html"

    def get_queryset(self):
        return Mission.objects.filter(
                author=self.request.user
            ).order_by('-date')


class EditReport(generic.UpdateView):
    model = Mission
    fields = [
        "date",
        "pay",
        "summary",
        "location",
        "type",
        "participants",
    ]
    template_name_suffix = "_update"
    success_url = "/my_reports"

    def form_valid(self, form):
        messages.success(self.request, 'Mission updated successfully.')
        return super().form_valid(form)


class CreateReport(generic.CreateView):
    model = Mission
    fields = [
        "date",
        "pay",
        "summary",
        "location",
        "type",
        "participants",
    ]
    template_name_suffix = "_create"
    success_url = "/my_reports"

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Mission created successfully.')
        return super().form_valid(form)


class DeleteReport(generic.DeleteView):
    model = Mission
    template_name_suffix = "_delete"
    success_url = "/my_reports"

    def form_valid(self, form):
        messages.success(self.request, 'Mission deleted successfully.')
        return super().form_valid(form)
