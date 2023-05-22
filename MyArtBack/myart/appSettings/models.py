from django.db import models

# Create your models here.
class Settings(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, default="settings_name")
    value = models.CharField(max_length=255, blank=True, null=False, default="")
    
    def __str__(self):
        return self.name