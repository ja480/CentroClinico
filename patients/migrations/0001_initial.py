# Generated by Django 4.1.4 on 2022-12-12 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(choices=[('MAS', 'Masculino'), ('FEM', 'Femenino')], max_length=9)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultingroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='doctors.consultingroom')),
                ('diary', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='doctors.diary')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='patients.patient')),
            ],
            options={
                'unique_together': {('diary', 'patient')},
            },
        ),
    ]
