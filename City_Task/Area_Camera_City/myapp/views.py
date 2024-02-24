from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404

from myapp.models import MappedTable,Area,City,Camera
from myapp.serializers import MappedSerializer,AreaSerializer,CameraSerializer,CitySerializer

class MappedView(APIView):
    
#################### GET Method ###############
    def get(self, request, *args, **kwargs):
        # Get the parameter based on the URL pattern
        area_id = kwargs.get('area_id')
        camera_id = kwargs.get('camera_id')
        city_id = kwargs.get('city_id')

        # Filter the queryset based on the provided parameter
        if area_id:
            our_data = MappedTable.objects.filter(area_ids__area_id=area_id)
        elif camera_id:
            our_data = MappedTable.objects.filter(camera_ids__camera_id=camera_id)
        elif city_id:
            our_data = MappedTable.objects.filter(city_ids__city_id=city_id)
        else:
            return Response({'status': 'error', 'message': 'Invalid URL pattern'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = MappedSerializer(our_data, many=True)
        return Response({'status': 'success', 'our_data': serializer.data}, status=status.HTTP_200_OK)

#################### POST Method ###############

######### Post Method For Area ##############
class AreaInsert(APIView):
    def post(self, request, format=None):
        serializer = AreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Retrieve the instance from the serializer
            instance = serializer.instance
            # Construct the response with the actual area_id value
            response_data = {
                'msg': "Area Details Upload Successfully.",
                'status': 'success',
                'our_data': {
                    'area_name': instance.area_name,
                    'area_id': instance.area_id,
                    'area_status': instance.area_status
                }
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response({'msg': "Invalid data", 'status': 'error', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


######### Post Method For City ##############
class CityInsert(APIView):
    def post(self, request, format=None):
        serializer = CitySerializer(data=request.data)  # Use CitySerializer here
        if serializer.is_valid():
            serializer.save()
            # Retrieve the instance from the serializer
            instance = serializer.instance
            # Construct the response with the actual city_id value
            response_data = {
                'msg': "City Details Upload Successfully.",
                'status': 'success',
                'our_data': {
                    'city_name': instance.city_name,
                    'city_id': instance.city_id,
                    'city_status': instance.city_status
                }
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response({'msg': "Invalid data", 'status': 'error', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


######### Post Method For Camera ##############

class CameraInsert(APIView):
    def post(self, request, format=None):
        serializer = CameraSerializer(data=request.data)  # Use CitySerializer here
        if serializer.is_valid():
            serializer.save()
            # Retrieve the instance from the serializer
            instance = serializer.instance
            # Construct the response with the actual city_id value
            response_data = {
                'msg': "Camera Details Upload Successfully.",
                'status': 'success',
                'our_data': {
                    'camera_name': instance.camera_name,
                    'camera_id': instance.camera_id,
                    'camera_status': instance.camera_status
                }
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response({'msg': "Invalid data", 'status': 'error', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



################## Delete Method For City ####################
class DeleteCity(APIView):
    def delete(self, request, city_id, format=None):
        try:
            city = City.objects.get(city_id=city_id)
            city.delete()
            return Response({'msg': "City deleted successfully.", 'status': 'success'}, status=status.HTTP_200_OK)
        except City.DoesNotExist:
            return Response({'msg': "City not found.", 'status': 'error'}, status=status.HTTP_404_NOT_FOUND)


################## Delete Method For Area ####################
class DeleteArea(APIView):
    def delete(self, request, area_id, format=None): 
        try:
            area = Area.objects.get(area_id=area_id)
            area.delete()
            return Response({'msg': "Area deleted successfully.", 'status': 'success'}, status=status.HTTP_200_OK)
        except Area.DoesNotExist:
            return Response({'msg': "Area not found.", 'status': 'error'}, status=status.HTTP_404_NOT_FOUND)

################## Delete Method For Camera ####################
class DeleteCamera(APIView):
    def delete(self, request, camera_id, format=None):
        try:
            camera = Camera.objects.get(camera_id=camera_id)
            camera.delete()
            return Response({'msg': "Camera deleted successfully.", 'status': 'success'}, status=status.HTTP_200_OK)
        except Camera.DoesNotExist:
            return Response({'msg': "Camera not found.", 'status': 'error'}, status=status.HTTP_404_NOT_FOUND)


################## Update  Method For Area ####################
################## put  Method For Area ####################
class UpdateArea(APIView):
     def get(self, request, area_id, format=None):
        try:
            area = get_object_or_404(Area, area_id=area_id)
            serializer = AreaSerializer(area)
            return Response({'Exting Data': serializer.data, 'status': 'success'}, status=status.HTTP_200_OK)
        except Area.DoesNotExist:
            return Response({'msg': "Area not found.", 'status': 'error'}, status=status.HTTP_404_NOT_FOUND)
     def patch(self, request, area_id, format=None):
        try:
            area = get_object_or_404(Area, area_id=area_id)
            if request.method == 'GET':
                serializer = AreaSerializer(area)
                return Response({'data': serializer.data, 'status': 'success'}, status=status.HTTP_200_OK)
            elif request.method == 'PATCH':
                serializer = AreaSerializer(area, data=request.data, partial=True)
                
                if serializer.is_valid():
                    serializer.save()
                    return Response({'msg': "Area updated successfully.", 'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
                
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Area.DoesNotExist:
            return Response({'msg': "Area not found.", 'status': 'error'}, status=status.HTTP_404_NOT_FOUND)
        
############################ Update City ######################
class UpdateCity(APIView):
    def get(self, request, city_id, format=None):
        try:
            city = get_object_or_404(City, city_id=city_id)
            serializer = CitySerializer(city)
            return Response({'Existing Data': serializer.data, 'status': 'success'}, status=status.HTTP_200_OK)
        except City.DoesNotExist:
            return Response({'msg': "City not found.", 'status': 'error'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, city_id, format=None):
        try:
            city = get_object_or_404(City, city_id=city_id)
            if request.method == 'GET':
                serializer = CitySerializer(city)
                return Response({'data': serializer.data, 'status': 'success'}, status=status.HTTP_200_OK)
            elif request.method == 'PATCH':
                serializer = CitySerializer(city, data=request.data, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response({'msg': "City updated successfully.", 'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except City.DoesNotExist:
            return Response({'msg': "City not found.", 'status': 'error'}, status=status.HTTP_404_NOT_FOUND)



############################ Update Camera ######################

class UpdateCamera(APIView):
    def get(self, request, camera_id, format=None):
        try:
            camera = get_object_or_404(Camera, camera_id=camera_id)
            serializer = CameraSerializer(camera)
            return Response({'Existing Data': serializer.data, 'status': 'success'}, status=status.HTTP_200_OK)
        except Camera.DoesNotExist:
            return Response({'msg': "Camera not found.", 'status': 'error'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, camera_id, format=None):
        try:
            camera = get_object_or_404(Camera, camera_id=camera_id)
            if request.method == 'GET':
                serializer = CameraSerializer(camera)
                return Response({'data': serializer.data, 'status': 'success'}, status=status.HTTP_200_OK)
            elif request.method == 'PATCH':
                serializer = CameraSerializer(camera, data=request.data, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response({'msg': "Camera updated successfully.", 'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Camera.DoesNotExist:
            return Response({'msg': "Camera not found.", 'status': 'error'}, status=status.HTTP_404_NOT_FOUND)