from django.shortcuts import render, HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("hello world")

def cmdb(request):
    return HttpResponse("this is cmdb")
    
def asset(request, asset_id):
    return HttpResponse(f"this asset {asset_id}")
