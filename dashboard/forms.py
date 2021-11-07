from django.forms import ModelForm
from dashboard.models.lab_entry_model import LabEntry
from dashboard.models.vehicle_model import VehicleModel, VEHICLE_MODEL_FIELDS


class UpdateVehicleForm(ModelForm):
    class Meta:
        model = VehicleModel
        fields = list(VEHICLE_MODEL_FIELDS)


# class UpdateLabEntryForm(ModelForm):
#     class Meta:
#         model = LabEntry
#         exclude = ('vehicle',)





# class UpdateMulti(MultiModelForm):
#     form_classes = {
#         'vehicle': UpdateVehicleForm,
#         'lab_entry': UpdateLabEntryForm
#     }