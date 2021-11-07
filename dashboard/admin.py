from django.contrib import admin
from dashboard.models.lab_entry_model import LabEntry
from dashboard.models.vehicle_model import VehicleModel
from dashboard.models.customer_model import CustomerModel

admin.site.register(LabEntry)
admin.site.register(VehicleModel)
admin.site.register(CustomerModel)
