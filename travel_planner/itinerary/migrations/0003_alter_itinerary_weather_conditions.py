# Generated by Django 5.1.5 on 2025-02-08 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0002_remove_itinerary_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='weather_conditions',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
