# Generated by Django 5.1 on 2024-08-31 14:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CabinType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='cabins/')),
            ],
        ),
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ingredients', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='tour',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tour',
            name='start_date',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tours.tourdate'),
        ),
        migrations.AddField(
            model_name='tour',
            name='lunch',
            field=models.ManyToManyField(blank=True, to='tours.lunch'),
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('duration', models.DurationField()),
                ('photo', models.ManyToManyField(blank=True, to='tours.photo')),
            ],
        ),
        migrations.AddField(
            model_name='tour',
            name='route',
            field=models.ManyToManyField(blank=True, to='tours.route'),
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='images/')),
                ('amount_of_places', models.IntegerField()),
                ('cabin_types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.cabintype')),
            ],
        ),
        migrations.AddField(
            model_name='tour',
            name='ship',
            field=models.ManyToManyField(blank=True, to='tours.ship'),
        ),
    ]
