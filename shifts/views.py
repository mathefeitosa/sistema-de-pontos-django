from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

from .forms import ShiftForm

from .models import Shift

# Create your views here.


def shifts(request):
    shifts = Shift.objects.all()
    return render(request, 'shifts/list.html', {'shifts': shifts})


def create_shift(request):
    if request.method == "POST":
        form = ShiftForm(request.POST)
        if form.is_valid():
            shift = form.save()
            print('Shift salvo!')
        return redirect('shifts')
    else:
        form = ShiftForm()
        return render(request, 'shifts/create.html', {'form': form})


def close_shift(request):
    shifts = Shift.objects.filter(owner=request.user, is_open=True)
    if shifts:
        return render(request, 'shifts/close.html', {'shifts': shifts})
    else:
        return HttpResponse('Nenhum turno em aberto!')


def close_shift_id(request, id):
    shift = Shift.objects.get(id=id)
    if shift:
        shift.is_open = False
        shift.save()
        print(shift)
        return redirect('shifts')
    else:
        return HttpResponseNotFound('Shift not found!')
