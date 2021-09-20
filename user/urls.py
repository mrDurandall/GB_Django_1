from django.urls import path

from user.views import UserLoginView, UserLogoutView, UserRegistrationView, profile, verify, send_verify_email_again


app_name = 'user'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/', profile, name='profile'),
    path('verify/<email>/<activation_key>/', verify, name='verify'),
    path('another_verify/<email>/', send_verify_email_again, name='another_verify'),
]
