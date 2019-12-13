from django.shortcuts import render, redirect
from .tables import TweetTable,CommentTable
from .models import Tweet,Comment
from .forms import CreateTweet,CreateComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home_view(request):
    title = 'Home'
    
    return render(request,'Tweet/base.html',{'title':title})

def tweet_view(request):
    title='Tweets'
    table = TweetTable(Tweet.objects.all())
    return render(request,'Tweet/tweets.html',{'title':title, 'table': table})

@login_required
def tweet_detail_view(request,pk):
    tweet = Tweet.objects.get(id=pk)
    comments = CommentTable(Comment.objects.filter(tweet=tweet))

    if request.method == 'POST':
        form = CreateComment(request.POST)
        if form.is_valid(): 
            user = User.objects.get(id=request.user.id)
            tweet = Tweet.objects.get(id=tweet.id)
            comment = Comment(content=form.cleaned_data.get('content'),user=user,tweet=tweet)
            comment.save()
            return redirect('tweets')
    else:
        form = CreateComment()

    return render(request,'Tweet/detail.html',{'title':'DetailView','tweet':tweet,'comments':comments,'comment_form':form})

@login_required
def tweet_post_view(request):
    if request.method == 'POST':
        form = CreateTweet(request.POST)
        if form.is_valid(): 
            user = User.objects.get(id=request.user.id)
            tweet = Tweet(content=form.cleaned_data.get('content'),user=user)
            tweet.save()
            return redirect('tweets')
    else:
        form = CreateTweet()
    
    return render(request,'Tweet/post.html',{'form':form})

@login_required
def comment_post_view(request):
    if request.method == 'POST':
        form = CreateComment(request.POST)
        if form.is_valid(): 
            user = User.objects.get(id=request.user.id)
            tweet = Tweet.objects.get(id=request.tweet.id)
            tweet = Tweet(content=form.cleaned_data.get('content'),user=user,tweet=tweet)
            tweet.save()
            return redirect('tweets')
    else:
        form = CreateComment()
    
    return render(request,'Tweet/post.html',{'form':form})
