from django.db import models

class MiModelo(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.IntegerField()
class Meta:
    app_label= "pruebaapp"

# Create your models here.
