from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def pet_add(request: HttpRequest) -> HttpResponse:
    return render(request, 'pets/pet-add-page.html')

def pet_details(request: HttpRequest) -> HttpResponse:
    return render(request, 'pets/pet-details-page.html')

def pet_edit(request: HttpRequest) -> HttpResponse:
    return render(request, 'pets/pet-edit-page.html')

def pet_delete(request: HttpRequest) -> HttpResponse:
    return render(request, 'pets/pet-delete-page.html')


