from django.db import models

# Create your models here.
class ContactModel(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)    
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=100, blank=False)
    message = models.CharField(blank=False, max_length=500)
    
