from django.contrib import admin
from django.urls import path

from ready_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('equipment/', view_equipment, name='view_equipment'),
    path('hike/', hike, name='hike'),
    path('bike/', bike, name='bike'),
    path('water_rafting/', water_rafting, name='water_rafting'),
    path('bp/', bp, name='bp'),

    path('create_duffle.html/', create_duffle, name='create_duffle'),
    path('create_category.html/', create_category, name='create_category'),
    path('create_warehouse.html/', create_warehouse, name='create_warehouse'),
    path('add_to_hike.html/', add_to_hike, name='add_to_hike'),
    path('add_to_bike.html/', add_to_bike, name='add_to_bike'),
    path('add_to_water_rafting.html/', add_to_water_rafting, name='add_to_water_rafting'),
    path('add_to_bp.html/', add_to_bp, name='add_to_bp'),
]
