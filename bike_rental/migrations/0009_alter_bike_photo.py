# Generated by Django 5.1 on 2024-09-05 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_rental', '0008_remove_bike_photos_remove_client_email_bike_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]