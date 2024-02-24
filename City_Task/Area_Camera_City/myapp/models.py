from django.db import models

# Create your models here.

STATUS_CHOICES={
    "Active":"active",
    "Inactive":"inactive"
}
class Area(models.Model):
    area_id = models.BigAutoField(primary_key=True)
    area_name= models.CharField(max_length=50)
    area_status = models.CharField(max_length=8, choices=STATUS_CHOICES, default="active")

class Camera(models.Model):
    camera_id = models.BigAutoField(primary_key=True)
    camera_name=models.CharField(max_length=70)
    camera_status = models.CharField(max_length=8, choices=STATUS_CHOICES, default="active")

class City(models.Model):
    city_id = models.BigAutoField(primary_key=True)
    city_name=models.CharField(max_length=50)
    city_status = models.CharField(max_length=8, choices=STATUS_CHOICES, default="active")

class MappedTable(models.Model):
    map_id = models.BigAutoField(primary_key=True)
    area_ids = models.ForeignKey(Area, on_delete=models.CASCADE)
    camera_ids = models.ForeignKey(Camera, on_delete=models.CASCADE)
    city_ids = models.ForeignKey(City, on_delete=models.CASCADE)
    final_status = models.CharField(max_length=8, choices=STATUS_CHOICES, default="active")



