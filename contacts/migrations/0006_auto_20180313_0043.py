# Generated by Django 2.0.2 on 2018-03-13 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20180305_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='website',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='company',
            field=models.CharField(max_length=255),
        ),
    ]