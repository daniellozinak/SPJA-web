from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .tables import ProfileTable
from .models import Profile
from .forms import CreateUserForm,UpdateProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout

@login_required
def profile_view(request):
    user = User.objects.get(id=request.user.id)
    profile_table = ProfileTable(Profile.objects.filter(user=user))

    if request.method == 'POST':
        update_form = UpdateProfile(request.POST,instance=request.user.profile)
        if update_form.is_valid():
            update_form.save()
            return redirect('profile')
    else:
        update_form = UpdateProfile(instance=request.user.profile)


    return render(request,'user/profile.html',{'profile_table':profile_table,'update_form':update_form})

    

def register_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = str(form.cleaned_data.get('username'))
            user = User.objects.get(username=user_name)
            profile = Profile(user=user)
            profile.save()
            return redirect('login')
    else:
        form = CreateUserForm()
    
    return render(request,'user/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request,'user/login.html',{'form':form,'title':'login'})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')