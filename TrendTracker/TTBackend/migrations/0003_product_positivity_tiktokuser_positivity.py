# Generated by Django 4.1.4 on 2023-01-11 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TTBackend', '0002_tiktokuser_points_tiktokuser_tiktok_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='positivity',
            field=models.CharField(default='neutral', max_length=16),
        ),
        migrations.AddField(
            model_name='tiktokuser',
            name='positivity',
            field=models.CharField(default='neutral', max_length=16),
        ),
    ]
