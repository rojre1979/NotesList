# Generated by Django 4.1.6 on 2023-02-04 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notelist", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="notelist",
            name="completed",
            field=models.BooleanField(default=False),
        ),
    ]
