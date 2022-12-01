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
