# Generated by Django 4.1.3 on 2022-12-05 07:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('detail', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='projectImages')),
                ('Url', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('clientName', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
