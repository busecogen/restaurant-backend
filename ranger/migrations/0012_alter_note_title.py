# Generated by Django 4.2.4 on 2023-09-12 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranger', '0011_alter_case_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
