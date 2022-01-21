from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView, PasswordResetView
from . import views

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_settings/', UserEditView.as_view(), name='edit-settings'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success/', views.password_success, name='password-success'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show-profile'),
    path('<int:pk>/edit_profile/', EditProfilePageView.as_view(), name='edit-profile'),
    path('create_profile/', CreateProfilePageView.as_view(), name='create-profile'),
    #reset password by email https://www.youtube.com/watch?v=sFPcd6myZrY
    path('reset_password/', PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete', PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]