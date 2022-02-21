from django.db import models

# Create your models here.
class Project(models.Model):
    class Meta:
        ordering = ['-date_created']
    date_created = models.DateTimeField(auto_now=True)  # Autoadd field
    