from django.db import models

# Create your models here.


class Dashboard(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    crew = models.CharField(max_length=100)

    def get_absolute_url(self):
        print('Ok')