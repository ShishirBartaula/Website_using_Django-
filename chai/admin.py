from django.contrib import admin
#This code registers a Django model with the Django admin panel
#  so it can be managed through the admin interface.

from .models import chaiVarity  #Imports the  chaiVariy model class name from models.py
admin.site.register(chaiVarity)  #Registers the chaiVariy model with Django Admin

# Register your models here.
