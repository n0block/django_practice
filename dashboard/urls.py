from django.urls import path
from dashboard.views import lab_entry_update_view, lab_entry_creation_view, dashboard_view

urlpatterns = [
    path('', dashboard_view.DashboardView.as_view(), name='dashboard'),
    path('lab-entry/create/', lab_entry_creation_view.create, name='lab-entry-create'),
    # path('lab-entry/<int:pk>/update/', lab_entry_update_view.UpdateLabEntryView.as_view(), name='lab-entry-update'),
]
