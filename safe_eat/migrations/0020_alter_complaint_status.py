# Generated by Django 5.0.2 on 2024-11-13 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_eat', '0019_complaint_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(choices=[('resolved', 'Resolved'), ('in_process', 'In Process'), ('fake', 'Fake'), ('pending', 'Pending')], default='Pending', max_length=20),
        ),
    ]
