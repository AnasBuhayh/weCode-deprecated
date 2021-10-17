from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User 
from django import forms
from .models import Profile

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'twitter_url', 'facebook_url', 'github_url')

        labels = {
        "bio": "السيرة الذاتية",
        "profile_pic": "الصورة الشخصية",
        "website_url": "الموقع الشخصي",
        "twitter_url": "Twitter",
        "facebook_url": "Facebook",
        "github_url": "GitHub",
        }

        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control'}),
            #make sure it's an image
            'profile_pic': forms.FileInput(attrs={'class':'form-control'}),
            'website_url': forms.TextInput(attrs={'class':'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class':'form-control'}),
            'github_url': forms.TextInput(attrs={'class':'form-control'}),
        }

        


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
    
        labels = {
            "first_name": "الإسم",
            "last_name": "اللقب",
            "email": "البريد الإلكتروني",
            }
        

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control','size': '20'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','size': '20'}),
            'email': forms.EmailInput(attrs={'class':'form-control','size': '40'}),
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        self.fields['username'].label = "إسم المستخدم"
        self.fields['password1'].label = "كلمة المرور"
        self.fields['password2'].label = "تأكيد كلمة المرور"


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','password')

    labels = {
        "first_name": "الإسم الأول",
        "last_name": "اللقب",
        "email": "البريد الإلكتروني",
        "password": "كلمة المرور",
        }

    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

class PasswordChangeingForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')

    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

    