from django.shortcuts import render, HttpResponse
from .models import Host
# Create your views here.
def index(request):
    host_list = Host.objects.all()
    return render(request, 'main.html', {'host_list': host_list})

def cmdb(request):
    return HttpResponse("this is cmdb")

def asset(request, asset_id):
    return HttpResponse(f"this asset {asset_id}")