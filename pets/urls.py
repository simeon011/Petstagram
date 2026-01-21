from django.urls import path, include

from pets import views

app_name = 'pets'

pets_patter = [
    path('', views.pet_details, name='pet_details'),
    path('edit/', views.pet_edit, name='pet-details'),
    path('delete/', views.pet_delete, name='pet-delete')
]

urlpatterns = [
    path('', views.pet_add, name='pet-add'),
    path('<str:username>/pet/<slug:pet_slug>/', include(pets_patter)),

]