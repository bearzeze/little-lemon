# Generated by Django 4.1.7 on 2023-03-23 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='inventory',
            field=models.SmallIntegerField(default=1),
        ),
    ]
