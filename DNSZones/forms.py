# -*- coding: utf-8 -*-
# forms.py
from django import forms
from django.forms.models import modelformset_factory
from .models import Zone, ResourceRecord
from django.shortcuts import get_object_or_404

ttl_choices = [(30, '30 секунд'), 
				(60, '1 минута'), 
				(1800, '30 минут'), 
				(3600, '1 час'),
				(3*3600, '3 часа')]

class ResourceRecordForm(forms.ModelForm):
	class Meta:
		model = ResourceRecord
		fields = '__all__'
		widgets = {
		'zone': forms.widgets.Select(attrs={'readonly' : 'true', 'hidden' : 'true'}),
		'ttl': forms.widgets.Select(choices=ttl_choices)
		}

ResourceRecordBase = modelformset_factory(ResourceRecord, 
	form=ResourceRecordForm, extra=1, exclude=())

class ResourceRecordFormSet(ResourceRecordBase):
	def __init__(self, *args, **kwargs):
		self.zone_name = kwargs.pop('zone_name')

		super(ResourceRecordFormSet, self).__init__(*args, **kwargs)
		z = get_object_or_404(Zone, name=self.zone_name)
		self.queryset = ResourceRecord.objects.filter(zone=z)
		self.initial = [{'zone': z,},]		
		for form in self.forms:
			form.empty_permitted = False