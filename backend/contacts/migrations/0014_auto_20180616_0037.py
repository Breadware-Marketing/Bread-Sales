# Generated by Django 2.0.2 on 2018-06-16 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0013_auto_20180615_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='employee_name',
        ),
        migrations.AddField(
            model_name='company',
            name='employee_first_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='company',
            name='employee_last_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
