from django import forms
from django.forms.widgets import TextInput, Select
from .models import Host, Agent

class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        exclude = ("id",)
        widgets = {
            'hostname': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;', 'placeholder': u'必填项'}),
            'ip': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;', 'placeholder': u'必填项'}),
            'cpu': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;', 'placeholder': u'可选项目'}),
            'mem': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;', 'placeholder': u'可选项目'}),
            'disk': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;', 'placeholder': u'可选项目'}),
            'desc': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;', 'placeholder': u'可选项目'}),
        }

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        exclude = ("id",)
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;', 'placeholder': u'必填项'}),
            'version': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;', 'placeholder': u'可选项目'}),
            'status': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;', 'placeholder': u'可选项目'}),
            'host': Select(attrs={'class': 'form-control', 'style': 'width:530px;'}),
        }
