from operator import imod

from django.urls import path,include
from .views import welcome, about

urlpatterns = [
    path('', welcome, name="welcome"),
    path('about', about),
    path('meeting/',include('meetings.urls'))
]
