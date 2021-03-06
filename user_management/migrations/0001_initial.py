# Generated by Django 2.2.6 on 2020-02-10 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orient_advances', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('image', models.ImageField(default='default.png', upload_to='profile_img')),
                ('employee_id', models.CharField(max_length=10, unique=True)),
                ('is_boss', models.BooleanField(blank=True, default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Last Login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orient_advances.Section')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', upload_to='profile_img')),
                ('employee_id', models.IntegerField(null=True, unique=True)),
                ('is_boss', models.BooleanField(default=False)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orient_advances.Section')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
