# Generated by Django 5.1.1 on 2024-11-06 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0002_review"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="movie",
            new_name="book",
        ),
    ]