# Generated by Django 4.2.6 on 2023-10-25 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0016_alter_image_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="image",
            field=models.ImageField(blank=True, upload_to="static/images"),
        ),
    ]
