# Generated by Django 4.1.4 on 2023-01-14 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TTBackend', '0004_tiktokuser_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiktokuser',
            name='hashtags',
            field=models.CharField(default='', max_length=4096),
        ),
        migrations.AddField(
            model_name='tiktokuser',
            name='nouns',
            field=models.CharField(default='', max_length=4096),
        ),
    ]
