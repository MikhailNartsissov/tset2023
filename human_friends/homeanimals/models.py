from django.db import models


# Таблица классов животных
class AnimalClass(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, default="Название класса животных")
    description = models.TextField(blank=True, null=False)


# Таблица команд
class Commands(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)


# Таблица животных
class Animal(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, default="Название животного")
    animal_class = models.ForeignKey(AnimalClass, on_delete=models.PROTECT)
    commands = models.ManyToManyField(Commands, related_name="animals")
    birth_date = models.DateField()
