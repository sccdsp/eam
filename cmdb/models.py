from django.db import models
from django.db.models import CharField, GenericIPAddressField

class Host(models.Model):
    hostname = CharField(max_length=255, verbose_name="主机名", unique=True, blank=False)
    ip = GenericIPAddressField(verbose_name="IP地址", blank=False)
    disk = models.CharField(max_length=255, null=True, blank=True)
    mem = models.CharField(max_length=255, null=True, blank=True)
    cpu = models.CharField(max_length=255, null=True, blank=True)
    desc = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.hostname

class Agent(models.Model):
    name = models.CharField(max_length=255, verbose_name="Agent名称", unique=True, blank=False)
    version = models.CharField(max_length=64, verbose_name="版本", blank=True)
    host = models.ForeignKey(Host, on_delete=models.CASCADE, related_name='agents', verbose_name="关联主机")
    status = models.CharField(max_length=32, verbose_name="状态", blank=True)
    last_heartbeat = models.DateTimeField(null=True, blank=True, verbose_name="最近心跳时间")

    def __str__(self):
        return self.name
