# Generated by Django 4.1.1 on 2022-12-03 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorname', models.CharField(max_length=50)),
                ('doctoremail', models.EmailField(max_length=50)),
                ('patientname', models.CharField(max_length=50)),
                ('patientemail', models.EmailField(max_length=50)),
                ('appointmentdate', models.DateField(max_length=10)),
                ('appointmenttime', models.TimeField(max_length=10)),
                ('symptoms', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('prescription', models.CharField(max_length=200)),
            ],
        ),
    ]
