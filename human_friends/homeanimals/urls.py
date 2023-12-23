from django.urls import path
from .views import ha_index

app_name = 'homeanimals'
urlpatterns = [
    path("", ha_index, name='index'),
]

