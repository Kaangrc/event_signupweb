# Generated by Django 5.0.7 on 2024-07-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventApp', '0002_remove_registration_phone_registration_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='gender',
            field=models.CharField(choices=[('B', 'Bay'), ('K', 'Bayan')], max_length=1),
        ),
    ]
