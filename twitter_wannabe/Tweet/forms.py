from django import forms
from django.contrib.auth.models import User
from .models import Tweet,Comment


class CreateTweet(forms.ModelForm):
    class Meta:
        model = Tweet
        fields=['content']

class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['content']