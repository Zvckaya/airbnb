# Generated by Django 2.2.5 on 2020-01-03 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0001_initial'),
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='rooms',
            field=models.ManyToManyField(blank=True, to='rooms.Room'),
        ),
    ]
