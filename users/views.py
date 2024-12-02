from django.shortcuts import render
from djang.http import HttpResponse

# Create your views here.
def home_page_view(request):
    return HttpResponse("<h1> Hello World!</h1>")