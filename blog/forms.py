from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Post
        fields = ('text', 'image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ImageUploadForm(forms.Form):
    image = forms.ImageField()
    
