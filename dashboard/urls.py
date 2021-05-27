from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('add/', views.dashboard_add, name='dashboard-add'),
]
