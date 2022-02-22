from django.db import models
from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL, DO_NOTHING
from django.contrib.auth.models import User
from django.dispatch import receiver

import re

# Create your models here.


class Project(models.Model):
    class Meta:
        ordering = ['-date_created']

    name = models.CharField(max_length=100, blank=False)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True)
    demo_link = models.URLField(max_length=200, blank=True)
    github_link = models.URLField(max_length=200, blank=True)
    # display_image = models.ImageField(upload_to='images/', blank=True)
    # image_gallery = models.ImageField(upload_to='images/', blank=True)

    date_created = models.DateTimeField(auto_now=True)  # Autoadd field

    def __str__(self):
        return ("{}".format(self.name))
