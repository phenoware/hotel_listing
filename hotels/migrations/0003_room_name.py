# Generated by Django 4.1.4 on 2023-02-13 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_rename_sleep_room_adults_room_childrens_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
