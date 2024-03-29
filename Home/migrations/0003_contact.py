# Generated by Django 5.0 on 2023-12-22 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('file', models.FileField(upload_to='contact_form_files')),
            ],
        ),
    ]
