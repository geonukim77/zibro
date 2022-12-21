# Generated by Django 3.2.8 on 2021-10-10 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_value', models.CharField(max_length=80, verbose_name='주택가격')),
                ('house_spec', models.CharField(max_length=80, verbose_name='스펙')),
                ('house_adress', models.CharField(max_length=80, verbose_name='주소')),
                ('house_content', models.TextField(verbose_name='설명')),
                ('created_at', models.DateTimeField(verbose_name='업데이트 날짜')),
                ('house_basic', models.TextField(verbose_name='기본정보')),
                ('contact_imform', models.TextField(verbose_name='연락처')),
                ('is_view', models.BooleanField(default=True, verbose_name='공개 여부')),
                ('house_photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
