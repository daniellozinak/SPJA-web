from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tweet(models.Model):
    content = models.CharField(max_length=420)
    date = models.DateField(default=timezone.now())
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content[:10]

class Comment(models.Model):
    content = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet,on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:10]