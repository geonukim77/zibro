# Generated by Django 4.1.3 on 2022-12-12 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zips', '0014_alter_zip_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='house_image',
            new_name='sub_image',
        ),
    ]
