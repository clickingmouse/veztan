#from django.db import models
from djongo import models
from jsonfield import JSONField

# Create your models here.
class Address(models.Model):
  #Created_At = models.DateTimeField(auto_now_add=True)
  #RequestAddress = modes.
  jsonLine = JSONField()
  
  def __str__(self):

    return self.jsonLine

  class Meta:
    verbose_name_plural = 'addresses'