# Generated by Django 5.0.1 on 2024-02-13 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0005_alter_recipe_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]