from django.urls import path
from .views import login_view, register_view, logout_view, students_list_view, employees_list_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('students/', students_list_view, name='student_list'),
    path('employees/', employees_list_view, name='employee_list'),
]
