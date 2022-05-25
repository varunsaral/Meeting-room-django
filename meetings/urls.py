from django.urls import path
from .views import *

urlpatterns = [
    path('rooms', room_list, name="room_list"),
    path('<int:id>', meeting_detail, name="meeting_detail"),
    path('new',new,name="new")
]
    