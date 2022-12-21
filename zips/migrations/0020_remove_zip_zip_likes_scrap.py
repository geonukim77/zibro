# Generated by Django 4.1.3 on 2022-12-19 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zips', '0019_zip_zip_likes_delete_scrap'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zip',
            name='zip_likes',
        ),
        migrations.CreateModel(
            name='Scrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('zip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zips.zip')),
            ],
        ),
    ]
