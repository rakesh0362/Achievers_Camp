# Generated by Django 3.1.5 on 2021-02-27 06:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('achievers', '0004_examnotification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examnotification',
            name='acivity',
        ),
        migrations.RemoveField(
            model_name='examnotification',
            name='examDate',
        ),
        migrations.AddField(
            model_name='examnotification',
            name='acivityDes',
            field=models.TextField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]