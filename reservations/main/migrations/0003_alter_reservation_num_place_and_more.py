# Generated by Django 4.2 on 2024-04-21 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='num_place',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='num_reservation',
            field=models.IntegerField(),
        ),
    ]
