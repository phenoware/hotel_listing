# Generated by Django 4.1.4 on 2023-02-12 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='status',
            field=models.CharField(default='new', max_length=50),
        ),
    ]
