# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# модель DNS-зоны
class Zone(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=255, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

rr_choices = [(t, t) for t in ("NS", "A", "CNAME", "TXT")]

# модель записи в DNS-зоне
class ResourceRecord(models.Model):
	zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	rr_type = models.CharField(choices=rr_choices, max_length=16)
	value = models.TextField()
	ttl = models.PositiveIntegerField() # TTL записи в секундах

	def __str__(self):
		return "%s.%s %s #%i" % (self.name, self.zone.name, self.rr_type, self.id)