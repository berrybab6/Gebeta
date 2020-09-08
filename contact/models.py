from django.db import models

# Create your models here.
class Comment(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    
    tel_number=models.CharField(max_length=16)
    email=models.EmailField()
    contact_me=models.BooleanField()
    contact_me_by=models.CharField(max_length=100)
    feedback=models.TextField()

