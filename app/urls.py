from django.urls import path
from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    path('universities/', views.universities, name='universities'),
    path('universities/<int:university_id>/', views.university, name='university'),
    path('create_university/', views.create_university, name='create_university'),
    path('delete_university/<int:university_id>/', views.delete_university, name='delete_university'),
]