# Generated by Django 5.0.7 on 2024-07-26 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='phone',
        ),
        migrations.AddField(
            model_name='registration',
            name='phone_number',
            field=models.CharField(default='0000000000', max_length=15),
        ),
    ]
