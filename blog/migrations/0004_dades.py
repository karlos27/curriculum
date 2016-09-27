# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160926_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('cognoms', models.CharField(max_length=150)),
                ('dni', models.CharField(max_length=9)),
                ('data_naixament', models.DateTimeField(null=True)),
                ('adreça', models.CharField(max_length=350)),
                ('telefon', models.CharField(max_length=9)),
                ('mail', models.CharField(max_length=200)),
                ('poblacio', models.CharField(max_length=100)),
                ('observacions', models.TextField()),
            ],
        ),
    ]
