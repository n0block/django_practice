from django.db import models


VEHICLE_META_FIELDS = (
    'manufacturer',
    'model',
    'VIN',
)

VEHICLE_FIELDS = (
    'manufacturer',
    'model',
    'VIN',
)


class VehicleModel(models.Model):
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    VIN = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.manufacturer} {self.model}'
