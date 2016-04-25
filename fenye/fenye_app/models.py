from __future__ import unicode_literals

from django.db import models


# Create your models here.

class host(models.Model):
	hostname = models.CharField(max_length=20)
	ip = models.GenericIPAddressField()
