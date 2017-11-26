from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/addlike/$', views.add_like, name='add_like'),
    url(r'^profiles/subscribe/(?P<targetuser>\S+)/$', views.subscribe_to_user, name='subscribe_to_user'),
    url(r'^profiles/unsubscribe/(?P<targetuser>\S+)/$', views.unsubscribe_to_user, name='unsubscribe_to_user'),
    url(r'^profiles/(?P<userp>\S+)/$', views.user_profile, name='user_profile'),
    url(r'^user_edit/$', views.user_edit, name='user_edit'),
]
