from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from .forms import CreateUserForm, ProfileForm
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

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('profiles')


def profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/profiles_list.html', {'profiles': profiles})


def create_user(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o usuário no banco de dados
        return redirect("profiles")
    else:
        form = CreateUserForm()
        return render(request, "profiles/create_user.html", {"form": form})


def edit_profile(request, id):
    profile = Profile.objects.get(id=id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            print('Perfil atualizado!')
            return redirect('profiles')
        return HttpResponse(request, 'Invalid form data!')
    else:
        form = ProfileForm(instance=profile)
        return render(request, 'profiles/edit.html', {'form': form})
