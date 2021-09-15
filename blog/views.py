from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import AddPostForm, UpdatePostForm, AddCommentForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {
        'cats':cats.title().replace('-', ' '), 
        'category_posts':category_posts
        })


def CategoryListView(request):
    cat_names_list = Category.objects.all()
    return render(request, 'categories_list.html', {
        'cat_names_list':cat_names_list
        })

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    
    def get_context_data(self, *args, **kwargs):
        cat_names = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_names"] = cat_names
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    form = AddCommentForm

    def get_context_data(self, *args, **kwargs):
        # context = super(DetailView, self).get_context_data(*args, **kwargs)
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
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'add_category.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')