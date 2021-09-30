from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import AddPostForm, UpdatePostForm, AddCommentForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .serializers import PostSerializer
from hitcount.views import HitCountDetailView
from taggit.models import Tag


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # paginate_by = 1
    
    def get_context_data(self, **kwargs):
        posts = Post.objects.order_by('-post_date')
        featured = posts.filter(featured=True).order_by('-post_date')[:2]
        featured_categories = posts.filter(featured=True).order_by('-post_date')[:3]
        popular = posts.order_by('-views')[:6]
        
        context = super().get_context_data(**kwargs)
        context = {
            'posts' : posts,
            'featured': featured,
            'popular': popular,
            'featured_categories': featured_categories,
        }

        return context

    # Get category names
    # def get_context_data(self, *args, **kwargs):
    #     cat_names = Category.objects.all()
    #     context = super(HomeView, self).get_context_data(*args, **kwargs)
    #     context["cat_names"] = cat_names
    #     return context

class CategoryView(ListView):
    model = Post
    template_name = 'categories.html'

    def get_context_data(self, **kwargs):
        posts = Post.objects.filter(category__slug=self.kwargs["category_slug"]).order_by('-post_date')
        featured = posts.filter(featured=True)[:1]
        popular = posts.order_by('-hit_count_generic__hits')[:3]

        context = super().get_context_data(**kwargs)
        context = {
            'posts' : posts,
            'featured': featured,
            'popular': popular,
        }

        return context


class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'post_detail.html'
    form = AddCommentForm
    count_hit = True

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["form"] = self.form
        return context

    def post(self, request, *args, **kwargs):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(request.META['HTTP_REFERER'])


class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'add_post.html'

    # gets the user id
    def form_valid(self, form):
        print(form)
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


# gets posts for vue paginator <not currently used>
@api_view(['GET'])
def GetPosts(request):
    posts = Post.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 3
    results = paginator.paginate_queryset(posts, request)

    serializer = PostSerializer(results, many=True)

    return paginator.get_paginated_response(serializer.data)