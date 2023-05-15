from django.db import models
from django.conf import settings
import os

def images_path():
    return os.path.join(settings.STATIC_ROOT)
#width_field=100, height_field=100
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')