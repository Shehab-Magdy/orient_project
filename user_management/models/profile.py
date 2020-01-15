from django.db import models
from django.contrib.auth.models import User
from orient_advances.models import Section
class Profile(models.Model):
    """Model definition for Profile."""

    # TODO: Define fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png',upload_to='media/profile_img')
    employee_id = models.IntegerField(unique=True)
    is_boos = models.IntegerField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of Profile."""
        return f'{self.User.username} Profile'
