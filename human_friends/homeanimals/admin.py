from django.contrib import admin
from .models import (
    AnimalClass,
    Animal,
    Commands,
)

admin.site.register(AnimalClass)
admin.site.register(Commands)
admin.site.register(Animal)
