from django.http import HttpResponse
from django.shortcuts import redirect, render

from profiles.forms import ProfileForm

# Create your views here.
def profiles(request):
    return HttpResponse("Profiles page!")


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
