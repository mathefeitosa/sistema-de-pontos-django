from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from profiles.forms import ProfileForm
from .models import Profile

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            print('Usuário não existe!')
        
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
    return render(request, 'login.html')

def logou_user(request):
    logout(request)
    return redirect('profiles')


def profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/profiles_list.html', {'profiles':profiles})


def create_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            print("Usuário salvo!")
        return redirect("profiles")
    else:
        form = ProfileForm()
        return render(request, "profiles/create.html", {"form": form})
