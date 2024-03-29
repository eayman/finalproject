# Generated by Django 4.1.7 on 2023-03-17 20:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('NID', models.PositiveIntegerField(unique=True, verbose_name='National Identification Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('address', models.CharField(blank=True, choices=[('Gaza', 'Gaza'), ('North Gaza', 'North Gaza'), ('Central', 'Central'), ('Khan Yunis', ' Khan Yunis'), ('Rafah', 'Rafah')], max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, help_text='enter details', max_length=250, null=True)),
                ('speed', models.PositiveSmallIntegerField(choices=[(4, 4), (8, 8), (32, 32), (16, 16)])),
                ('duration', models.PositiveSmallIntegerField(choices=[(6, 6), (1, 1), (12, 12), (3, 3)])),
                ('month_cost', models.PositiveSmallIntegerField()),
                ('is_popular', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
                ('plan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clients.plan')),
            ],
        ),
    ]
