# Generated by Django 4.2.3 on 2023-08-18 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('phone', models.PositiveIntegerField()),
                ('caddress', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('registration', models.PositiveIntegerField()),
                ('mileage', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('image1', models.ImageField(upload_to='ad_images/')),
                ('image2', models.ImageField(upload_to='ad_images/')),
                ('image3', models.ImageField(upload_to='ad_images/')),
                ('image4', models.ImageField(upload_to='ad_images/')),
                ('image5', models.ImageField(upload_to='ad_images/')),
            ],
        ),
        migrations.CreateModel(
            name='UserCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=50)),
                ('car_model', models.CharField(max_length=50)),
                ('client_name', models.CharField(max_length=100)),
                ('client_mobile', models.CharField(max_length=20)),
                ('client_address', models.TextField()),
                ('car_problem', models.TextField()),
                ('booking_date', models.DateField()),
            ],
        ),
    ]
