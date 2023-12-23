from django.urls import path
from .views import (
    AnimalsListView,
    AnimalCreateView,
    AnimalDetailsView,
    AnimalUpdateView,
    AnimalDeleteView,
)


app_name = 'homeanimals'
urlpatterns = [
    path("", AnimalsListView.as_view(), name="animals_list"),
    path("create/", AnimalCreateView.as_view(), name="animal_create"),
    path("<int:pk>/", AnimalDetailsView.as_view(), name="animal_details"),
    path("<int:pk>/update/", AnimalUpdateView.as_view(), name="animal_update"),
    path("<int:pk>/delete/", AnimalDeleteView.as_view(), name="animal_delete"),
]
