# Generated by Django 4.2.16 on 2024-12-07 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0002_alter_about_options_about_history_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="about",
            name="company_statement",
            field=models.TextField(
                default="Empowering nomads and redefining urban mobility."
            ),
        ),
    ]