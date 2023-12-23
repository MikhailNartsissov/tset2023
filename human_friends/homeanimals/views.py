from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import (
    Animal,
    AnimalClass,
    AnimalBreed,
    Commands,
)
from django.shortcuts import reverse


class AnimalsListView(ListView):
    template_name = 'homeanimals/animals-list.html'
    model = Animal
    context_object_name = 'animals'


class AnimalDetailsView(DetailView):
    template_name = 'homeanimals/animal_detail.html'
    model = Animal
    context_object_name = 'animal'


class AnimalCreateView(CreateView):
    model = Animal
    fields = "name", "animal_class", "animal_breed", "birth_date", "commands"
    success_url = reverse_lazy('homeanimals:animals_list')


class AnimalUpdateView(UpdateView):
    model = Animal
    fields = "name", "animal_class", "animal_breed", "birth_date", "commands"
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse(
            'homeanimals:animal_details',
            kwargs={"pk": self.object.pk},
        )


class AnimalDeleteView(DeleteView):
    model = Animal
    success_url = reverse_lazy('homeanimals:animals_list')