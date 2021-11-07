from django_tables2 import SingleTableView

from dashboard.models.lab_entry_model import LabEntry
from dashboard.tables import DashboardTable


class DashboardView(SingleTableView):
    model = LabEntry
    table_class = DashboardTable
    template_name = 'dashboard/dashboard.html'
