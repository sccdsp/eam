from django.contrib import admin
from django.urls import path, include
from cmdb import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cmdb.urls")),
]
