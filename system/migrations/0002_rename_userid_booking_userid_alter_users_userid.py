# Generated by Django 5.0 on 2024-02-21 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='UserID',
            new_name='UserId',
        ),
        migrations.AlterField(
            model_name='users',
            name='UserId',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]
