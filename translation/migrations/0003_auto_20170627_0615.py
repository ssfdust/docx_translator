# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-27 06:15
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0002_docx_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docx_file',
            name='file_path',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/uploads/', location='/home/ssfdust/website/uploads'), upload_to=''),
        ),
    ]