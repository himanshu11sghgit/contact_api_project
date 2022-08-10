from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField()
    country_code = models.IntegerField()
    contact_picture = models.URLField(null=True)
    is_favorite = models.BooleanField(default=False)