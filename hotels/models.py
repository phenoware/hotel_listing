from django.db import models
import slugify
from partner.models import *
from ckeditor.fields import RichTextField
# Create your models here.

class Facilities(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    icon = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name


class Property(models.Model):
    id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(Partner, on_delete=models.CASCADE)

    AddedDate = models.DateTimeField(auto_now_add=True)
    lastUpdateDate = models.DateTimeField(null=True, blank=True)

    name = models.CharField(max_length=200, default='')
    slug = models.SlugField(max_length=200, unique=True)
    propertyType = models.CharField(max_length=100, default='')
    # Location Details 
    address = models.TextField(default='')
    city = models.CharField(max_length=100, default='')
    pincode = models.IntegerField(default=0, null=True)
    state = models.CharField(max_length=100, default='')

    # Property Details 
    overview = models.TextField(default='', null=True)
    image = models.ImageField(upload_to='proprty/images', null=True, blank= True)
    videoLink = models.CharField(max_length=200, default='')
    priceMin = models.IntegerField(null=True, default=0)
    priceMax = models.IntegerField(null=True, default=0)

    checkInFrom = models.CharField(max_length=100, default='')
    checkOutUntil = models.CharField(max_length=100, default='')    

    receptionOpenFrom = models.CharField(max_length=100, default='')
    receptionOpenUntil = models.CharField(max_length=100, default='')

    status = models.CharField(max_length=100, default='under-review')

    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify.slugify(self.name)
        super().save(*args, **kwargs)

class PropertyFacilities(models.Model):
    id = models.AutoField(primary_key=True)
    facilities = models.ForeignKey(Facilities, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    
class PropertyImages(models.Model):
    id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='proprty/images', null=True, blank= True)
    addedDate = models.DateTimeField(auto_now_add=True)

class RoomFeatures(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    
    addedDate = models.DateTimeField(auto_now_add=True)
    lastUpdate = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=100, default='')
    status = models.CharField(max_length=100, default='')

    roomType = models.CharField(max_length=100, default='')#AC/NON AC
    image = models.ImageField(upload_to='proprty/images/room', null=True, blank= True)
    price = models.IntegerField(null=True, default=0)
    adults = models.IntegerField(null=True, default=0)
    childrens = models.IntegerField(null=True, default=0)

    priceIncludes = models.ManyToManyField(RoomFeatures, through='RoomPriceIncludes')

class RoomPriceIncludes(models.Model):
    id = models.AutoField(primary_key=True)
    roomFeatures = models.ForeignKey(RoomFeatures, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    

