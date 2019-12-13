from django.urls import path
from . import views

urlpatterns=[
    path('',views.home_view,name='home'),
    path('tweets/',views.tweet_view,name='tweets'),
    path('detail/<int:pk>',views.tweet_detail_view,name='detail'),
    path('post/',views.tweet_post_view,name='post'),
]