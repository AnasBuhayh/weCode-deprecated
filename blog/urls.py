from django.urls import path
# from . import views
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<str:slug>', PostDetailView.as_view(), name='post-detail'),
    path('post/<str:slug>/addcomment', PostDetailView.as_view(), name='add-comment'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('add_category/', AddCategoryView.as_view(), name='add-category'),
    path('update_post/<str:slug>', UpdatePostView.as_view(), name='update-post'),
    path('post/<str:slug>/delete', DeletePostView.as_view(), name='delete-post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('categories/', CategoryListView, name='categories')
]
