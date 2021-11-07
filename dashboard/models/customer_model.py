from django.db import models


CUSTOMER_MODEL_FIELDS = (
    'name',
    'address',
    'representative',
    'social_security_number',
    'telephone'
)


class CustomerModel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    representative = models.CharField(max_length=100)
    social_security_number = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
