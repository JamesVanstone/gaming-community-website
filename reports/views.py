from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Mission

# Create your views here.
#def home_page_view(request):
    #return HttpResponse("<h1> Hello World!</h1>")

class HomePage(generic.ListView):
    queryset = Mission.objects.all().order_by('-date')[:3]
    template_name = "reports/home_page.html"

class MissionsPage(generic.ListView):
    queryset = Mission.objects.all()
    paginate_by = 2
    model = Mission
    template_name = "reports/missions_page.html"