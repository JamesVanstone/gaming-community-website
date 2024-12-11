from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('missions', views.MissionsPage.as_view(), name='missions'),
    path('my_reports', views.MyReportsPage.as_view(), name='myreports'),
    path('mission/<int:pk>/edit/', views.EditReport.as_view(), name='mission-edit'),
    path('mission/create/', views.CreateReport.as_view(), name='mission-create'),
    path('mission/<int:pk>/delete/', views.DeleteReport.as_view(), name='mission-delete'),
]