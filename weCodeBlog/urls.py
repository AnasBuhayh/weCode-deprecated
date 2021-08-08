from django.urls import path
# from . import views
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView

urlpatterns = [
    # path('', views.home, name="home")
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('add_category/', AddCategoryView.as_view(), name='add-category'),
    path('update_post/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete-post'),
    path('category/<str:cats>/', CategoryView, name='category')
]
