from django.db import models
from django.contrib import admin

# Create your models here.
class colours(models.Model):
    colour= models.CharField(max_length=200)
    colourcode= models.CharField(max_length=600)

class coloursAdmin(admin.ModelAdmin):
    list_display=('colour','colourcode')