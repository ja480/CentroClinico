<<<<<<< Updated upstream
# Generated by Django 4.1.1 on 2022-12-01 15:23
=======
# Generated by Django 4.1 on 2022-12-01 18:21
>>>>>>> Stashed changes

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CentroClinico', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='password',
        ),
    ]
