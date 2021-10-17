from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy, reverse
from .forms import SignUpForm, EditProfileForm, PasswordChangeingForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, CreateView
from .models import Profile
from blog.models import Post
from .forms import ProfilePageForm

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile.html'

    # gets the user id
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    
    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        user_posts = Post.objects.filter(author__profile__id=self.kwargs['pk']).order_by('-post_date')
        context = {
            'page_user' : page_user,
            'user_posts' : user_posts
        }    

        return context   

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    form_class = ProfilePageForm
    #fields = ['bio', 'profile_pic', 'website_url', 'twitter_url', 'facebook_url', 'github_url']
    success_url = reverse_lazy('home')

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeingForm
    success_url = reverse_lazy('password-success')

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

def password_success(request):
    return render(request, 'registration/password_success.html', {})


