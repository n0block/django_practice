from django.db import models


RESULTS_FIELDS = (
    'CO2',
)


class ResultsModel(models.Model):
    CO2 = models.IntegerField(default=0)

