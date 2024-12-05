# Generated by Django 4.2.16 on 2024-12-05 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="about",
            options={
                "verbose_name": "About Section",
                "verbose_name_plural": "About Section",
            },
        ),
        migrations.AddField(
            model_name="about",
            name="history",
            field=models.TextField(
                default="Founded with the goal of redefining urban mobility, we partner with leading brands to deliver innovative solutions."
            ),
        ),
        migrations.AlterField(
            model_name="about",
            name="mission",
            field=models.TextField(
                default="Our mission is to empower digital nomads and adventurers with stylish, durable, and minimalist products."
            ),
        ),
        migrations.AlterField(
            model_name="about",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="about",
            name="vision",
            field=models.TextField(
                default="To become the go-to platform for digital nomads seeking premium everyday carry solutions."
            ),
        ),
    ]