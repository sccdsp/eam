from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("edit/<int:pk>/", views.edit, name="edit"),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('collect/', views.collect, name='collect'),
    path("agents/", views.agent_list, name="agent_list"),
    path("agents/add/", views.agent_add, name="agent_add"),
    path("agents/edit/<int:pk>/", views.agent_edit, name="agent_edit"),
    path("agents/delete/<int:pk>/", views.agent_delete, name="agent_delete"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
]
