from django.shortcuts import redirect, render
from .forms import WorkplacesForm
from .models import Workplaces

# Create your views here.
def workplaces(request):
  workplaces = Workplaces.objects.all()
  return render(request, 'workplaces/list.html', {'workplaces':workplaces})

def create_workplaces(request):
  if request.method == 'POST':
    form = WorkplacesForm(request.POST)
    if form.is_valid():
      workplace = form.save()
      print('Workplace salvo!')
      return redirect('workplaces')
  else:
    form = WorkplacesForm()
    return render(request, 'workplaces/create.html', {'form':form})