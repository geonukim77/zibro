# Generated by Django 3.2.7 on 2021-12-03 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zips', '0010_auto_20211202_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='house_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='zip',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
