# Generated by Django 2.2.6 on 2020-01-15 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_boos',
        ),
        migrations.AddField(
            model_name='profile',
            name='is_boss',
            field=models.BooleanField(default=False),
        ),
    ]
