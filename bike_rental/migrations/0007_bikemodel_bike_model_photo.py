# Generated by Django 5.1 on 2024-09-05 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_rental', '0006_client_alter_bikemodel_options_bike_price_per_day_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikemodel',
            name='bike_model_photo',
            field=models.ImageField(blank=True, null=True, upload_to='bike_model_photos/'),
        ),
    ]