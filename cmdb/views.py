from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Host, Agent
from .forms import HostForm, AgentForm
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

def delete(request, pk):
    host = get_object_or_404(Host, pk=pk)
    if request.method == "POST":
        host.delete()
        return redirect('index')
    return redirect('index')

@csrf_exempt
def collect(request):
    """
    资产采集接口
    :param request:
    :字典格式为:
    {
        "hostname": "host1",
        "ip": "192.168.1.1",
        "disk": "100G",
        "mem": "16G",
        "cpu": "intel xeon e5-2630 v4",
        "desc": "web server"
    }
    :return:
    """
    asset_info = json.loads(request.body)
    if request.method == "POST":
        hostname = asset_info.get('hostname')
        ip = asset_info.get('ip')
        disk = asset_info.get('disk')
        mem = asset_info.get('mem')
        cpu = asset_info.get('cpu')
        desc = asset_info.get('desc')
        try:
            host = Host.objects.get(hostname=hostname)
        except Host.DoesNotExist:
            host = Host()
        host.hostname = hostname
        host.ip = ip
        host.disk = disk
        host.mem = mem
        host.cpu = cpu
        host.desc = desc
        host.save()
    return HttpResponse('success')

def agent_list(request):
    agents = Agent.objects.select_related('host').all()
    return render(request, 'agent_list.html', {'agents': agents})

def agent_add(request):
    if request.method == "POST":
        form = AgentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agent_list')
    else:
        form = AgentForm()
    return render(request, 'agent_edit.html', {'form': form})

def agent_edit(request, pk):
    agent = get_object_or_404(Agent, pk=pk)
    if request.method == "POST":
        form = AgentForm(request.POST, instance=agent)
        if form.is_valid():
            form.save()
            return redirect('agent_list')
    else:
        form = AgentForm(instance=agent)
    return render(request, 'agent_edit.html', {'form': form, 'agent': agent})

def agent_delete(request, pk):
    agent = get_object_or_404(Agent, pk=pk)
    if request.method == "POST":
        agent.delete()
        return redirect('agent_list')
    return redirect('agent_list')

