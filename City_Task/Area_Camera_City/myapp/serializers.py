from rest_framework import serializers
from myapp.models import MappedTable, Area, Camera, City

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['area_name', 'area_status']

class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ['camera_name', 'camera_status']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name', 'city_status']

class MappedSerializer(serializers.ModelSerializer):
    our_data = serializers.SerializerMethodField()

    class Meta:
        model = MappedTable
        fields = ['our_data']

    def get_our_data(self, obj):
        return {
            "area_name": obj.area_ids.area_name,
            "camera_name": obj.camera_ids.camera_name,
            "city_name": obj.city_ids.city_name,
            "area_status": obj.area_ids.area_status,
        }

    def to_representation(self, instance):
        # If the request has 'area_id', 'camera_id', or 'city_id' in the context,
        # filter the queryset accordingly
        request = self.context.get('request')
        if request and 'area_id' in request.GET:
            instance = instance.filter(area_ids__area_id=request.GET['area_id'])
        elif request and 'camera_id' in request.GET:
            instance = instance.filter(camera_ids__camera_id=request.GET['camera_id'])
        elif request and 'city_id' in request.GET:
            instance = instance.filter(city_ids__city_id=request.GET['city_id'])

        return super().to_representation(instance)
