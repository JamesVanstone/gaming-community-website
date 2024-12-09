from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Mission

# Create your views here.
#def home_page_view(request):
    #return HttpResponse("<h1> Hello World!</h1>")

class HomePage(generic.ListView):
    queryset = Mission.objects.all()
    template_name = "home_page.html"