from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
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
            return redirect('index')
    else:
        form = HostForm()
    return render(request, 'add.html', {'form': form})

def edit(request, pk):
    host = get_object_or_404(Host, pk=pk)
    if request.method == "POST":
        form = HostForm(request.POST, instance=host)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = HostForm(instance=host)
    return render(request, 'edit.html', {'form': form, 'host': host})
