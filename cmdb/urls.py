from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cmdb/", views.cmdb, name="cmdb"),
    path("cmdb/asset/<int:asset_id>/", views.asset, name="asset"),
]
