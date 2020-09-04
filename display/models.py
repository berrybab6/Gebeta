from django.db import models

# Create your models here.
class Food(models.Model):
    F_name=models.CharField(max_length=100)
    F_desc=models.TextField()
    F_img=models.ImageField(upload_to='pics')
    isTraditional=models.BooleanField(default=False)
    promot=models.BooleanField(default=False)
    price=models.FloatField(default=0.0)

class Chief(models.Model):
    chief_name=models.CharField(max_length=100)
    description=models.TextField()
    chief_img=models.ImageField(upload_to='pics')
    exprience=models.PositiveIntegerField()
    role=models.CharField(max_length=200)
    awards_num=models.PositiveIntegerField(null=True)
    award_types=models.CharField(max_length=150,null=True,default=" ")
    points=models.PositiveIntegerField(default=0)


    