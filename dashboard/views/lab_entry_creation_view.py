from django.http.response import HttpResponseRedirect
from django.template.response import TemplateResponse

from dashboard.forms.lab_entry_creation_form import LabEntryForm


def create(request):
    lb_inst = LabEntryForm()

    if request.method == 'POST':
        lb_inst.save(request)
        return HttpResponseRedirect('/dashboard')

    else:
        context = lb_inst.forms_factory()

    return TemplateResponse(request, 'dashboard/create.html', context)
