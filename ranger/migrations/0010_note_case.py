# Generated by Django 4.2.4 on 2023-09-11 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ranger', '0009_rename_menu_case_menus'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='case',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ranger.case'),
        ),
    ]
