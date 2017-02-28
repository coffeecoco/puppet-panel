# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 10:55
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(b'^[\\w:]+$', b'Characters must match regex [\\w:]+', b'invalid')])),
            ],
            options={
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(b'^[\\w-]+$', b'Characters must match regex [\\w-]+', b'invalid')])),
                ('classes', models.ManyToManyField(blank=True, to='puppet.Class')),
                ('parents', models.ManyToManyField(blank=True, to='puppet.Group')),
            ],
        ),
        migrations.CreateModel(
            name='GroupParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(b'^[\\w:.-]+$', b'Characters must match regex [\\w:.-]+', b'invalid')])),
                ('value', models.TextField(blank=True, null=True)),
                ('encryption_key', models.CharField(blank=True, max_length=512, null=True)),
                ('encrypted', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='puppet.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(b'^[a-zA-Z0-9.-]+$', b'Characters must match regex [a-zA-Z0-9.-]+', b'invalid')])),
                ('classes', models.ManyToManyField(blank=True, to='puppet.Class')),
                ('groups', models.ManyToManyField(blank=True, to='puppet.Group')),
            ],
        ),
        migrations.CreateModel(
            name='NodeParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(b'^[\\w:.-]+$', b'Characters must match regex [\\w:.-]+', b'invalid')])),
                ('value', models.TextField(blank=True, null=True)),
                ('encryption_key', models.CharField(blank=True, max_length=512, null=True)),
                ('encrypted', models.BooleanField(default=False)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='puppet.Node')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='nodeparameter',
            unique_together=set([('name', 'node')]),
        ),
        migrations.AlterUniqueTogether(
            name='groupparameter',
            unique_together=set([('name', 'group')]),
        ),
    ]
