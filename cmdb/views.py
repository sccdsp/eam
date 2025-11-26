from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .models import Host
from .forms import HostForm
# Create your views here.
def index(request):
    host_list = Host.objects.all()
    return render(request, 'main.html', {'host_list': host_list})

def add(request):
    if request.method == "POST":
        form = HostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = HostForm()
    return render(request, 'add.html', {'form': form})
