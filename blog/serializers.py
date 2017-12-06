from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post, Comment, Profile

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'password', 'first_name', 'email')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('pk','author', 'text', 'postpic','created_date', 'likedone')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('pk','post', 'author', 'text', 'created_date')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('pk','user', 'profpic', 'subscribers','subscribes', 'description')
