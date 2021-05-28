from django.shortcuts import render, redirect
from django_tables2 import SingleTableView
from django.views.generic import UpdateView

from .forms import CrewMemberForm, UpdateCrewMemberForm
from .models import Dashboard
from .tables import DashboardTable


from django.http import HttpResponse

# Create your views here.


def dashboard_add(request):
    if request.method == 'POST':
        form = CrewMemberForm(request.POST)
        form.save()
        return redirect('dashboard')

    else:
        form = CrewMemberForm()
        return render(request, 'dashboard/add.html', {'form': form})


class UpdateCrewMemberView(UpdateView):
    model = Dashboard
    fields = ['first_name', 'second_name', 'crew']
    template_name = 'dashboard/update.html'



# def dashboard_update(request):
#     if request.method == 'POST':
#         form = UpdateCrewMemberForm(request.POST)
#         form.save()
#         return redirect('dashboard')
#
#     else:
#         form = UpdateCrewMemberForm()
#         return render(request, 'dashboard/update.html', {'form': form})


class DashboardView(SingleTableView):
    model = Dashboard
    table_class = DashboardTable
    template_name = 'dashboard/dashboard.html'



