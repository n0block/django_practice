
from django.views.generic import UpdateView

from dashboard.models.lab_entry_model import LabEntry
# from dashboard.forms.lab_entry_form import LabEntryForm


# class UpdateLabEntryView(UpdateView):
#     model = LabEntry
#     form_class = LabEntryForm
#     template_name = 'dashboard/update.html'
#
#     def get_form_kwargs(self):
#         kwargs = super(UpdateLabEntryView, self).get_form_kwargs()
#         kwargs.update(instance={
#             'vehicle_meta': self.object.vehicle,
#             'owner_meta': self.object.owner,
#         })
#         return kwargs
