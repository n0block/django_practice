import django_tables2 as tables
from dashboard.models.lab_entry_model import LabEntry, LAB_ENTRY_FIELDS


class DashboardTable(tables.Table):

    class Meta:
        model = LabEntry
        template_name = 'django_tables2/bootstrap.html'
        fields = ('id',) + LAB_ENTRY_FIELDS
        attrs = {'class': 'table table-hover'}
        row_attrs = {
            # 'onclick': "window.location.href = {{ url 'update' record.pk }}",
            'onclick': 'myFunction(this)',
            'style': 'cursor: pointer',
        }
