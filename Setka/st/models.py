from django.db import models

class Setka(models.Model):
    ves = models.FloatField(default=3.6)
    dlina = models.FloatField(default=150)
    unitl = models.CharField(max_length= 10,default='cm')
    razmer_romba = models.FloatField(default= 3.6)
    unitr = models.CharField(max_length=10,default='mm')
    price = models.DecimalField(max_digits= 10,decimal_places= 2)
