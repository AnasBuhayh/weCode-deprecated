from django.contrib import admin
from .models import Post, Category
from members.models import Profile

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)