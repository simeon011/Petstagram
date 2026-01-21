from django.contrib import admin
from unfold.admin import ModelAdmin

from photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(ModelAdmin):
    list_display = ['id', 'description', 'date_of_published', 'tagged_pets_list']

    @staticmethod
    def tagged_pets_list(obj):
        return ', '.join(pet.name for pet in obj.tagged_pets.all())
