# Generated by Django 4.2.6 on 2023-10-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0018_alter_image_image"),
    ]

    operations = [
        migrations.RemoveField(model_name="about", name="image",),
        migrations.AddField(
            model_name="project",
            name="image_tag",
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.DeleteModel(name="Image",),
    ]