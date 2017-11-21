from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    author = models.ForeignKey('auth.User', blank = True)
    text = models.TextField()
    postpic = models.ImageField(null = True,
        verbose_name=u'Photo')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            default=timezone.now)
    likes = models.IntegerField(verbose_name='Like', default=0)
    likedone = models.ManyToManyField(User, related_name='users_likes', blank = True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.postpic.url

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profpic = models.ImageField(blank = True, default='default_profile_picture.png',
        verbose_name=u'profoto')
    subscribers = models.ManyToManyField(User, related_name='subscribers', blank = True)
    subscribes = models.ManyToManyField(User, related_name='subscribes', blank = True)
    description = models.TextField(default = "")
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
       if created:
          Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
