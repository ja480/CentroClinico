# Generated by Django 4.1 on 2022-12-07 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CentroClinico', '0013_rename_doctore_doctor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]
