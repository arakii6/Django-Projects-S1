# Generated by Django 5.0.1 on 2024-01-08 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0003_recipe_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_view_count',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]