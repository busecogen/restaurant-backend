# Generated by Django 4.2.4 on 2023-09-11 16:55

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranger', '0007_casemenurelation'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='menu',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None),
        ),
        migrations.DeleteModel(
            name='CaseMenuRelation',
        ),
    ]