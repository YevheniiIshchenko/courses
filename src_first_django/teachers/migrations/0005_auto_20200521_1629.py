# Generated by Django 2.2.12 on 2020-05-21 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_remove_logger_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='logger',
            name='created',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='logger',
            name='method',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='logger',
            name='path',
            field=models.CharField(default='', max_length=256),
        ),
    ]
