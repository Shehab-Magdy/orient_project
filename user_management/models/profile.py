from django.db import models
from django.contrib.auth.models import User
from orient_advances.models import Section

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png',upload_to='profile_img')
    employee_id = models.IntegerField(unique=True)
    is_boss = models.BooleanField(default=False)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.user.username} Profile'
