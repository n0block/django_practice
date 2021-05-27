from django.shortcuts import render, redirect
from django_tables2 import SingleTableView
from .forms import CrewMemberForm
from .models import Dashboard
from .tables import DashboardTable


from django.http import HttpResponse

# Create your views here.


def dashboard_add(request):
    print('MORON')
    if request.method == 'POST':
        form = CrewMemberForm(request.POST)
        form.save()
        return redirect('dashboard')

    else:
        form = CrewMemberForm()
        return render(request, 'dashboard/add.html', {'form': form})


class DashboardView(SingleTableView):
    model = Dashboard
    table_class = DashboardTable
    template_name = 'dashboard/dashboard.html'



