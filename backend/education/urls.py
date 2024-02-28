from django.urls import path
from .views import faculty_list, department_list, managment_list

urlpatterns = [
    path('faculty/', faculty_list, name='faculty'),
    path('departament/', department_list, name='departament'),
    path('managment/', managment_list, name='managment'),
]
