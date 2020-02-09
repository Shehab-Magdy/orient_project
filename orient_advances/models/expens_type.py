from django.db import models


class Expens(models.Model):
    expens_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.expens_name
