# -*- coding: utf-8 -*-
#views.py
from .forms import ResourceRecordFormSet
from django.shortcuts import render
from django.contrib import messages
from .models import Zone, ResourceRecord

def manage_resources(request, zone_name):
	if request.method == 'POST':
		formset = ResourceRecordFormSet(zone_name=zone_name, data=request.POST)
		if formset.is_valid():
			formset.save()
			messages.success(request, 'You have updated your zone resources.')
	else:
		formset = ResourceRecordFormSet(zone_name=zone_name, initial=[{'zone': Zone.objects.get(name=zone_name),},])
		messages.info(request, 'Edit zone resources:')
	return render(request, "zoneresources.html", 
		{"formset": formset, "zone_name": zone_name})
	