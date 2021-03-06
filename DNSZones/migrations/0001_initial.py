# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-26 12:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rr_type', models.CharField(choices=[(b'NS', b'NS'), (b'A', b'A'), (b'CNAME', b'CNAME'), (b'TXT', b'TXT')], max_length=16)),
                ('value', models.TextField()),
                ('ttl', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='resourcerecord',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DNSZones.Zone'),
        ),
    ]
