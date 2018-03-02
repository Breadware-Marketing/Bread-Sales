# Generated by Django 2.0.2 on 2018-03-02 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='address_2',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='company',
            name='employees',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.URLField(default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='location',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]
