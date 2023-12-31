# Generated by Django 5.0 on 2023-12-23 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeanimals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalBreed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='animal_breed',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='homeanimals.animalbreed'),
        ),
    ]
