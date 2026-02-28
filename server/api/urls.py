from django.urls import path
from .views import signup, get_users

urlpatterns = [
    path('signup/', signup),
    path('users/', get_users),
]