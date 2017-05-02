# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 10:00
from __future__ import unicode_literals

import codenerix.fields
import codenerix.lib.helpers
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('identifier', models.CharField(blank=True, max_length=200, null=True, verbose_name='Identifier')),
                ('public', models.BooleanField(default=False, verbose_name='Public')),
                ('default', models.BooleanField(default=False, verbose_name='Default')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SliderElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('order', models.IntegerField(verbose_name='Order')),
                ('show_title', models.BooleanField(default=False, verbose_name='Show tittle')),
                ('public', models.BooleanField(default=False, verbose_name='Public')),
                ('html_format', models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=2, null=True, verbose_name='HtmlFormat')),
                ('new_price', models.CharField(blank=True, max_length=200, null=True, verbose_name='New price')),
                ('old_price', models.CharField(blank=True, max_length=200, null=True, verbose_name='Old price')),
                ('discount', models.CharField(blank=True, max_length=200, null=True, verbose_name='Discount')),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sliderelements', to='codenerix_cms.Slider', verbose_name='Slider')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SliderElementTextEN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('image', codenerix.fields.ImageAngularField(blank=True, max_length=200, null=True, upload_to=codenerix.lib.helpers.upload_path, verbose_name='Image')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('button', models.CharField(blank=True, max_length=200, null=True, verbose_name='Button')),
                ('url', models.CharField(max_length=500, verbose_name='URL')),
                ('slider_element', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='en', to='codenerix_cms.SliderElement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SliderElementTextES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('image', codenerix.fields.ImageAngularField(blank=True, max_length=200, null=True, upload_to=codenerix.lib.helpers.upload_path, verbose_name='Image')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('button', models.CharField(blank=True, max_length=200, null=True, verbose_name='Button')),
                ('url', models.CharField(max_length=500, verbose_name='URL')),
                ('slider_element', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='es', to='codenerix_cms.SliderElement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Staticheader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('identifier', models.CharField(blank=True, max_length=200, null=True, verbose_name='Identifier')),
                ('public', models.BooleanField(default=False, verbose_name='Public')),
                ('html_format', models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=2, null=True, verbose_name='HtmlFormat')),
                ('num_elements', models.IntegerField(verbose_name='Number of columns')),
                ('default', models.BooleanField(default=False, verbose_name='By default')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StaticheaderElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('order', models.IntegerField(verbose_name='Order')),
                ('show_title', models.BooleanField(default=False, verbose_name='Show tittle')),
                ('public', models.BooleanField(default=False, verbose_name='Public')),
                ('frontheader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staticheaderelements', to='codenerix_cms.Staticheader', verbose_name='Static Header')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StaticheaderElementTextEN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('image', codenerix.fields.ImageAngularField(blank=True, max_length=200, null=True, upload_to=codenerix.lib.helpers.upload_path, verbose_name='Image')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('button', models.CharField(blank=True, max_length=200, null=True, verbose_name='Button')),
                ('url', models.CharField(max_length=500, verbose_name='URL')),
                ('staticheader_element', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='en', to='codenerix_cms.StaticheaderElement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StaticheaderElementTextES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('image', codenerix.fields.ImageAngularField(blank=True, max_length=200, null=True, upload_to=codenerix.lib.helpers.upload_path, verbose_name='Image')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('button', models.CharField(blank=True, max_length=200, null=True, verbose_name='Button')),
                ('url', models.CharField(max_length=500, verbose_name='URL')),
                ('staticheader_element', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='es', to='codenerix_cms.StaticheaderElement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('status', models.CharField(choices=[(b'D', 'Draft'), (b'R', 'Public'), (b'P', 'Pending')], default=b'D', max_length=150, verbose_name='Status')),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StaticPageTextEN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('slug', models.CharField(max_length=200, unique=True, verbose_name='slug')),
                ('tiles', codenerix.fields.MultiBlockWysiwygField(blank=True, verbose_name='Tiles')),
                ('static_page', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='en', to='codenerix_cms.StaticPage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StaticPageTextES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('slug', models.CharField(max_length=200, unique=True, verbose_name='slug')),
                ('tiles', codenerix.fields.MultiBlockWysiwygField(blank=True, verbose_name='Tiles')),
                ('static_page', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='es', to='codenerix_cms.StaticPage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TemplateStaticPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('template', models.TextField(verbose_name='Template')),
                ('tile', models.TextField(verbose_name='Tile')),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='staticpage',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staticpages', to='codenerix_cms.TemplateStaticPage'),
        ),
    ]