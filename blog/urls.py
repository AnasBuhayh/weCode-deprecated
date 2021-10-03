from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, CategoryView, LoadMore

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('load-more', LoadMore, name='load-more'),
    path('post/<str:slug>', PostDetailView.as_view(), name='post-detail'),
    path('post/<str:slug>/addcomment', PostDetailView.as_view(), name='add-comment'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('update_post/<str:slug>', UpdatePostView.as_view(), name='update-post'),
    path('post/<str:slug>/delete', DeletePostView.as_view(), name='delete-post'),
    path('category/<slug:category_slug>/', CategoryView.as_view(), name='category'),
]
