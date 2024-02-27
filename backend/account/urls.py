from django.urls import path
from .views import login_view, register_view, logout_view, user_list_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('user_list/', user_list_view, name='user_list'),
]
