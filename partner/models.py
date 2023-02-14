from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
import slugify
# Create your models here.


class Partner(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    businessName = models.CharField(max_length=200, default='')
    slug = models.SlugField(max_length=200, unique=True)
    password = models.CharField(max_length=100, default='Null')
    phone = models.CharField(max_length=50, default='Null')
    status = models.CharField(max_length=50, default='new')
    
    def __str__(self):
        return self.businessName

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify.slugify(self.businessName)
        super().save(*args, **kwargs)





