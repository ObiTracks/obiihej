from django.apps import apps
from django.contrib import admin
from .models import *

# Register your models here.
models = apps.get_models()

for model in models:
    try:
        if model.__name__ != "Club":
            admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
