# Generated by Django 5.1 on 2024-08-31 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additionaloption',
            name='tour',
        ),
        migrations.RemoveField(
            model_name='freeofchargeservice',
            name='tour',
        ),
        migrations.RemoveField(
            model_name='tourdate',
            name='tour',
        ),
        migrations.AddField(
            model_name='tour',
            name='additional_options',
            field=models.ManyToManyField(blank=True, to='tours.additionaloption'),
        ),
        migrations.AddField(
            model_name='tour',
            name='dates',
            field=models.ManyToManyField(blank=True, to='tours.tourdate'),
        ),
        migrations.AddField(
            model_name='tour',
            name='free_services',
            field=models.ManyToManyField(blank=True, to='tours.freeofchargeservice'),
        ),
    ]
