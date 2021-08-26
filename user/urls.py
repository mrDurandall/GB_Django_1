from django.urls import path

from user.views import login, logout, registration, profile


app_name = 'user'

urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('registration', registration, name='registration'),
    path('profile', profile, name='profile')
]

