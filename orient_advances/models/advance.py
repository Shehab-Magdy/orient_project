from django.db import models
from user_management.models import Account

class Advance(models.Model):
    emplyee = models.ForeignKey(Account,on_delete=models.CASCADE)
    amount = models.FloatField(name='Advance amount', help_text='Amount should be in LE')
    request_date = models.DateField(name='Advance Date',auto_now=True)
   
    def __str__(self):
        return f"{self.emplyee.username} has requested {self.amount}"
