# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-07 09:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("hordak", "0002_check_leg_trigger_20160903_1149")]

    operations = [
        migrations.RunSQL(
            """ALTER TABLE hordak_leg ADD CONSTRAINT zero_amount_check CHECK (amount != 0)""",
            """ALTER TABLE hordak_leg DROP CONSTRAINT zero_amount_check""",
        )
    ]
