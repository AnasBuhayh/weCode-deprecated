from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name','name')
choices_list = []
for item in choices:
    choices_list.append(item)

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'tags', 'category', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'','id':'author','type':'hidden'}),
            'tags': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choices_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'header_image': forms.FileInput(attrs={'class':'form-control'}),
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tags', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'tags': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'})
        }
