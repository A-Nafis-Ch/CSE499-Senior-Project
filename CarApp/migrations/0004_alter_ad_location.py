# Generated by Django 4.2.3 on 2023-08-21 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarApp', '0003_ad_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='location',
            field=models.CharField(choices=[('Dhaka', 'Dhaka'), ('Chittagong', 'Chittagong'), ('Rajshahi', 'Rajshahi'), ('Sylhet', 'Sylhet'), ('Khulna', 'Khulna'), ('Barisal', 'Barisal'), ('Rangpur', 'Rangpur')], default='Dhaka', max_length=20),
        ),
    ]
