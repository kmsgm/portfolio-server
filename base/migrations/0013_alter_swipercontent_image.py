# Generated by Django 4.2.6 on 2023-10-24 05:14

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0012_swipercontent_rename_projects_project"),
    ]

    operations = [
        migrations.AlterField(
            model_name="swipercontent",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=base.models.upload_to
            ),
        ),
    ]
