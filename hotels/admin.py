from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Facilities)
admin.site.register(Property)
admin.site.register(PropertyImages)
admin.site.register(PropertyFacilities)
admin.site.register(RoomFeatures)
admin.site.register(RoomPriceIncludes)