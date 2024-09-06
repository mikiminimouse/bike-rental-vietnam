# Generated by Django 5.1 on 2024-09-05 22:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_rental', '0007_bikemodel_bike_model_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bike',
            name='photos',
        ),
        migrations.RemoveField(
            model_name='client',
            name='email',
        ),
        migrations.AddField(
            model_name='bike',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='bike_photos/'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='bike_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike_rental.bikemodel'),
        ),
        migrations.AlterField(
            model_name='client',
            name='contact',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]