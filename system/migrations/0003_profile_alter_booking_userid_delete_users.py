# Generated by Django 5.0 on 2024-02-22 20:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_rename_userid_booking_userid_alter_users_userid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('UserId', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('UserLevel', models.TextField(choices=[('Student', 'Student'), ('Lecturer', 'Lecturer')], max_length=30)),
                ('PhoneNo', models.CharField(max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='UserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.profile'),
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
