from django.db import models
from .vehicle_model import VehicleModel
from .customer_model import CustomerModel
from .results_model import ResultsModel

LAB_ENTRY_FIELDS = (
    "customer",
    "vehicle",
    "results"
)


class LabEntry(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.DO_NOTHING, blank=True)
    vehicle = models.ForeignKey(VehicleModel, on_delete=models.DO_NOTHING, blank=True)
    results = models.ForeignKey(ResultsModel, on_delete=models.DO_NOTHING, blank=True)

    @classmethod
    def create(cls, **kwargs):
        results_id = ResultsModel.objects.create()
        kwargs.update({"results": results_id})

        lab_entry = cls(**kwargs)
        return lab_entry
