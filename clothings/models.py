from django.db import models

# Create your models here.


class Clothing(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)


    def __str__(self):
        return self.summary

class Testing(models.Model):
    user = models.CharField(max_length=200)
