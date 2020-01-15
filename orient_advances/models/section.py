from django.db import models

class Section(models.Model):
    """Model definition for Section."""

    # TODO: Define fields here
    section_name = models.CharField(max_length=40,unique=True,name='Section name')
    class Meta:
        """Meta definition for Section."""

        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

    def __str__(self):
        """Unicode representation of Section."""
        return self.section_name
