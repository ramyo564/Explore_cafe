# Generated by Django 4.2.2 on 2023-06-19 23:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "city_name",
                    models.CharField(default="도시이름", max_length=50, unique=True),
                ),
                (
                    "slug",
                    models.SlugField(allow_unicode=True, max_length=100, unique=True),
                ),
            ],
            options={
                "verbose_name": "City",
                "verbose_name_plural": "Cities",
            },
        ),
    ]
