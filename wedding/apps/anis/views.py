from django.http import HttpResponse
from django.shortcuts import render
from .forms import FittingForm

def wedding(request):
    form = FittingForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(form)

    return render(request, 'anis/anis.html', locals())