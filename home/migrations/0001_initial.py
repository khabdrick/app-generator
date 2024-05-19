# Generated by Django 4.2.8 on 2024-05-19 09:44

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='name', unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]