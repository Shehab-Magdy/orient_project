from django.db import models

class Section(models.Model):
    section_name = models.CharField(max_length=40,unique=True)
   
    def __str__(self):
        return self.section_name
