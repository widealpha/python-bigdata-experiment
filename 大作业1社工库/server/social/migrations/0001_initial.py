# Generated by Django 3.1.7 on 2021-03-19 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_id', models.CharField(max_length=200)),
                ('use_astro', models.CharField(max_length=200)),
                ('use_nation', models.CharField(max_length=200)),
                ('use_school', models.CharField(max_length=200)),
                ('use_img', models.CharField(max_length=200)),
                ('use_age', models.CharField(max_length=200)),
                ('use_sex', models.CharField(max_length=200)),
                ('use_weibo', models.CharField(max_length=200)),
                ('use_email', models.CharField(max_length=200)),
                ('use_phone', models.CharField(max_length=200)),
                ('use_address', models.CharField(max_length=200)),
                ('use_appraise', models.CharField(max_length=200)),
                ('use_height', models.CharField(max_length=200)),
                ('use_real_name', models.CharField(max_length=200)),
                ('use_birthplace', models.CharField(max_length=200)),
            ],
        ),
    ]
