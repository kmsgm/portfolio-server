# Generated by Django 4.2.6 on 2023-10-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_home_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="about",
            name="image",
            field=models.ImageField(blank=True, upload_to="about/"),
        ),
    ]
