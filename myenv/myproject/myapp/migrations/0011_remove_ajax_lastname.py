# Generated by Django 5.0.2 on 2024-03-22 07:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0010_ajax"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ajax",
            name="lastname",
        ),
    ]
