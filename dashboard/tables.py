import django_tables2 as tables
from .models import Dashboard


class DashboardTable(tables.Table):

    class Meta:
        model = Dashboard
        template_name = 'django_tables2/bootstrap.html'
        fields = ('id', 'first_name', 'second_name', 'crew')
        attrs = {'class': 'table table-hover'}
        row_attrs = {
            # 'onclick': "window.location.href = {{ url 'update' record.pk }}",
            'onclick': 'myFunction(this)',
            'style': 'cursor: pointer',
        }
