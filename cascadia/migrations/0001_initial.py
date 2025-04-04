# Generated by Django 5.1.7 on 2025-03-20 16:27

import django.contrib.gis.db.models.fields
import django.contrib.postgres.operations
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        django.contrib.postgres.operations.CreateExtension(
            name="postgis",
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("geometry", django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                "verbose_name_plural": "cities",
                "ordering": ("name",),
            },
        ),
    ]
