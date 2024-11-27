# Generated by Django 5.0.2 on 2024-11-21 17:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_eat', '0030_contactmessage'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('account_type', models.CharField(choices=[('customer', 'customer'), ('admin', 'admin')], default='customer', max_length=10)),
                ('profile_picture', models.ImageField(blank=True, default='static/images/user-profile.png', null=True, upload_to='static/images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]