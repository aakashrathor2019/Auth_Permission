# Generated by Django 4.2.8 on 2024-09-25 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("name", models.CharField(max_length=50)),
                ("emp_id", models.ImageField(upload_to="")),
                ("pos", models.CharField(max_length=50)),
                ("joining_date", models.DateTimeField()),
            ],
        ),
    ]
