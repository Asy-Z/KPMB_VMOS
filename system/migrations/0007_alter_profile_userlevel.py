# Generated by Django 5.0 on 2024-02-25 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_alter_vehicle_vehicletype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='UserLevel',
            field=models.TextField(choices=[('Administrator', 'Administrator'), ('Student', 'Student'), ('Lecturer', 'Lecturer')], max_length=30),
        ),
    ]
