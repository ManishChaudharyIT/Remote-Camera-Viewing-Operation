from django.urls import path
from . import views

urlpatterns = [

    ############# FOR Get Methods Urls #####################
    path('area_details/<int:area_id>/', views.MappedView.as_view(), name="area_details"),
    path('camera_details/<int:camera_id>/', views.MappedView.as_view(), name="camera_details"),
    path('city_details/<int:city_id>/', views.MappedView.as_view(), name="city_details"),

    ############# FOR Post Methods Urls #####################
    path('area_insert_details/',views.AreaInsert.as_view(), name='area_insert_details'),
    path('city_insert_details/',views.CityInsert.as_view(), name='city_insert_details'),
    path('camera_insert_details/',views.CameraInsert.as_view(), name='camera_insert_details'),

    ############# FOR Delete Methods Urls #####################
    path('city_delete/<int:city_id>',views.DeleteCity.as_view(), name='city_delete'),
    path('area_delete/<int:area_id>',views.DeleteArea.as_view(), name='area_delete'),
    path('camera_delete/<int:camera_id>',views.DeleteCamera.as_view(), name='camera_delete'),

    ############# FOR Update Methods Urls #####################
    path('update_area/<int:area_id>/', views.UpdateArea.as_view(), name='update_area'),
    path('update_city/<int:city_id>/', views.UpdateCity.as_view(), name='update_city'),
    path('update_camera/<int:camera_id>/', views.UpdateCamera.as_view(), name='update_camera'),




]
