# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 17:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utubeu_viewer.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, verbose_name='Chatroom Name')),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('identifier', models.CharField(default=utubeu_viewer.models.generate_id_string, max_length=38)),
                ('is_public', models.BooleanField(default=False)),
                ('max_occupants', models.IntegerField(default=20, verbose_name='The maximum number of joiners')),
                ('duration', models.BigIntegerField(default=2700)),
                ('is_active', models.BooleanField(default=True)),
                ('start', models.DateTimeField(auto_now=True, verbose_name='When the user added the chatroom')),
                ('joiners', models.ManyToManyField(related_name='joined_chatrooms', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_chatrooms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSiteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_logged_in', models.BooleanField(default=False)),
                ('madeup_username', models.CharField(blank=True, max_length=30, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='site_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]