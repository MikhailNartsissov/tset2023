from django.contrib import admin
from .models import (
    AnimalClass,
    AnimalBreed,
    Animal,
    Commands,
)

admin.site.register(AnimalClass)
admin.site.register(Commands)
admin.site.register(AnimalBreed)
admin.site.register(Animal)
