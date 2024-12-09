from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('missions', views.MissionsPage.as_view(), name='missions'),
]