from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Mission

# Create your views here.
#def home_page_view(request):
    #return HttpResponse("<h1> Hello World!</h1>")

class HomePage(generic.ListView):
    queryset = Mission.objects.filter(approved=True).order_by('-date')[:3]
    template_name = "reports/home_page.html"

class MissionsPage(generic.ListView):
    queryset = Mission.objects.filter(approved=True)
    paginate_by = 2
    model = Mission
    template_name = "reports/missions_page.html"

class MyReportsPage(generic.ListView):
    model = Mission
    template_name = "reports/my_reports_page.html"
    def get_queryset(self):
        return Mission.objects.filter(author=self.request.user)