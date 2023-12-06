# Generated by Django 4.2.3 on 2023-10-25 06:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CarApp', '0004_alter_ad_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='user',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ad',
            name='location',
            field=models.CharField(choices=[('Dhaka', 'Dhaka'), ('Chittagong', 'Chittagong'), ('Rajshahi', 'Rajshahi'), ('Sylhet', 'Sylhet'), ('Khulna', 'Khulna'), ('Barisal', 'Barisal'), ('Rangpur', 'Rangpur')], max_length=20),
        ),
    ]