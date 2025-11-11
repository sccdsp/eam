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
