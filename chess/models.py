from django.db import models

# Create your models here.

class Time(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, blank = True, null= True) 
    color1 = models.CharField(max_length=100)
    color2 = models.CharField(max_length=100)
    branding = models.ImageField(upload_to='chess/', blank = True, null= True)

   
    def __str__(self):
        return self.nome