from django.shortcuts import redirect, render
from .forms import WorkplaceForm
from .models import Workplace

# Create your views here.


def workplaces(request):
    workplaces = Workplace.objects.all()
    return render(request, "workplaces/list.html", {"workplaces": workplaces})


def create_workplace(request):
    if request.method == "POST":
        form = WorkplaceForm(request.POST)
        if form.is_valid():
            workplace = form.save()
            print("Workplace salvo!")
            return redirect("workplaces")

    else:
        form = WorkplaceForm()
        return render(request, "workplaces/create.html", {"form": form})
