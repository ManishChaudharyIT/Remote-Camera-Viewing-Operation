from django.contrib import admin
from .models import Area,Camera,City,MappedTable

# Register your models here.
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display=['area_id','area_name','area_status']

@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display=['camera_id','camera_name','camera_status']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display=['city_id','city_name','city_status']

@admin.register(MappedTable)
class MappedAdmin(admin.ModelAdmin):
    list_display=['map_id','area_ids','camera_ids','city_ids']



