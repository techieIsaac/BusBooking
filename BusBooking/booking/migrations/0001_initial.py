# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-11 05:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.CharField(max_length=512)),
                ('cancelled', models.BooleanField(default=False)),
                ('rating', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('code', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256, unique=True)),
                ('rto_registration_number', models.CharField(max_length=256, unique=True)),
                ('type', models.CharField(choices=[('seater', 'Seater'), ('semi-sleeper', 'Semi Sleeper'), ('sleeper', 'Sleeper')], max_length=128)),
                ('ac', models.BooleanField(default=False)),
                ('double_berth', models.BooleanField(default=False)),
                ('num_rows', models.IntegerField()),
                ('num_lcols', models.IntegerField()),
                ('num_rcols', models.IntegerField()),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='busses', to='booking.Brand')),
            ],
            options={
                'verbose_name': 'Bus',
                'verbose_name_plural': 'Busses',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('code', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='booking.Bus')),
                ('from_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_schedules', to='booking.Location')),
                ('to_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_schedules', to='booking.Location')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='booking.Schedule'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL),
        ),
    ]
