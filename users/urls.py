from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success/', views.password_success, name='password-success'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show-profile-page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit-profile-page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create-profile-page'),
]