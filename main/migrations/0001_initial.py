# Generated by Django 4.2.7 on 2023-11-05 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Hospital Name')),
                ('location', models.CharField(choices=[('Urban', 'Urban'), ('Rural', 'Rural')], max_length=10, verbose_name='Location')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('ownership', models.CharField(choices=[('Government', 'Government'), ('Private', 'Private'), ('Non-Profit', 'Non-Profit')], max_length=15, verbose_name='Ownership')),
                ('ownership_type', models.CharField(max_length=255, verbose_name='Ownership Type')),
                ('facility_level', models.CharField(choices=[('Primary', 'Primary'), ('Secondary', 'Secondary'), ('Tertiary', 'Tertiary')], max_length=10, verbose_name='Facility Level')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Longitude')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Latitude')),
                ('ambulance_service', models.BooleanField(verbose_name='Ambulance Service')),
            ],
            options={
                'verbose_name_plural': 'Hospitals',
            },
        ),
    ]
