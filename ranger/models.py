from django.contrib import admin
from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)


class Case(models.Model):
    name = models.CharField(max_length=255, unique=True)
    menus = ArrayField(
        models.IntegerField(),
        null=True,
        blank=True
    )


class Note(models.Model):
    title = models.CharField(max_length=255)
    explanation = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE, default=None)

    class Meta:
        unique_together = ("title", "case")



admin.site.register(Note)
admin.site.register(Menu)
admin.site.register(Case)
