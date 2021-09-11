from django.urls import path

from user.views import UserLoginView, UserLogoutView, UserRegistrationView, ProfileView


app_name = 'user'

urlpatterns = [
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('registration', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile')
]

