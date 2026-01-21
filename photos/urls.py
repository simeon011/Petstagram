from django.urls import path, include

from photos import views

app_name = 'photos'

photo_patterns = [
    path('', views.detail_photo, name='detail-photo'),
    path('edit/', views.edit_photo, name='edit-photo'),
]

urlpatterns = [
    path('add/', views.add_photo, name='add-photo'),
    path('<int:pk>', include(photo_patterns)),
]