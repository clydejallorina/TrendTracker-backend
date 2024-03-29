# Generated by Django 4.1.4 on 2022-12-13 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=2048)),
                ('url', models.URLField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TiktokUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=128)),
                ('url', models.URLField(max_length=256)),
            ],
        ),
    ]
