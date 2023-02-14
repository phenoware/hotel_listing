# Generated by Django 4.1.4 on 2023-02-12 13:28

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partner', '0003_remove_partner_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('icon', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('AddedDate', models.DateTimeField(auto_now_add=True)),
                ('lastUpdateDate', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(default='', max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('propertyType', models.CharField(default='', max_length=100)),
                ('address', models.TextField(default='')),
                ('city', models.CharField(default='', max_length=100)),
                ('pincode', models.IntegerField(default=0, null=True)),
                ('state', models.CharField(default='', max_length=100)),
                ('overview', ckeditor.fields.RichTextField(default='', null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='proprty/images')),
                ('videoLink', models.CharField(default='', max_length=200)),
                ('priceMin', models.IntegerField(default=0, null=True)),
                ('priceMax', models.IntegerField(default=0, null=True)),
                ('checkInFrom', models.CharField(default='', max_length=100)),
                ('checkOutUntil', models.CharField(default='', max_length=100)),
                ('receptionOpenFrom', models.CharField(default='', max_length=100)),
                ('receptionOpenUntil', models.CharField(default='', max_length=100)),
                ('status', models.CharField(default='under-review', max_length=100)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.partner')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('addedDate', models.DateTimeField(auto_now_add=True)),
                ('lastUpdate', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='proprty/images/room')),
                ('roomType', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(default=0, null=True)),
                ('sleep', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomFeatures',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RoomPriceIncludes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.room')),
                ('roomFeatures', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.roomfeatures')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='priceIncludes',
            field=models.ManyToManyField(through='hotels.RoomPriceIncludes', to='hotels.roomfeatures'),
        ),
        migrations.AddField(
            model_name='room',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.property'),
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='proprty/images')),
                ('addedDate', models.DateTimeField(auto_now_add=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyFacilities',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('facilities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.facilities')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.property')),
            ],
        ),
    ]
