# Generated by Django 4.2.4 on 2023-09-07 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranger', '0002_menumodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumodel',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='menumodel',
            name='url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='notesmodel',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]