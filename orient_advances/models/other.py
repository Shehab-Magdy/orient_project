from django.db import models
from orient_project import settings
from user_management.models import Account
# from .other import other



class other(models.Model):
    emplyee_id = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2, help_text='Amount should be in LE')
    request_date = models.DateField(default='2018-1-1')
    description = models.TextField(null=True)

    def __str__(self):
        return str(self.amount)