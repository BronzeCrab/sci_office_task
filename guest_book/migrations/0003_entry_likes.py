# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest_book', '0002_remove_entry_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
