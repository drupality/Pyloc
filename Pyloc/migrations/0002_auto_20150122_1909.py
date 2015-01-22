# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pyloc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenueCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='venue',
            name='categories',
            field=models.ManyToManyField(to='Pyloc.VenueCategory'),
            preserve_default=True,
        ),
    ]
