from django import forms
from .models import Post, Category, Comment
import re

choices = Category.objects.all().values_list('name','name')
choices_list = []
for item in choices:
    choices_list.append(item)

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','summary', 'body', 'header_image', 'category', 'tags')

        labels = {
        "title": "العنوان",
        "tags": "العلامات",
        "category": "التصنيف",
        "summary":"الملخص",
        "body": "المحتوى",
        "header_image": "الغلاف",
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'tags': forms.TextInput(attrs={'class':'form-control', 'data-role':"tagsinput", 'name':"tags"}),
            'category': forms.Select(choices=choices_list, attrs={'class':'form-control'}),
            'summary': forms.TextInput(attrs={'class':'form-control'}),
            'header_image': forms.FileInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}), 
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'summary', 'body', 'category', 'tags')

        labels = {
        "title": "العنوان",
        "tags": "العلامات",
        "category": "التصنيف",
        "summary":"الملخص",
        "body": "المحتوى",
        "header_image": "الغلاف",
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'tags': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choices_list, attrs={'class':'form-control'}),
            'header_image': forms.FileInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        labels = {
        "body": "المحتوى",
        }

        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }