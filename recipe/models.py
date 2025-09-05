from django.db import models

# Create your models here.
class Receita(models.Model):
    name= models.CharField(max_length=100)
    ingredients= models.TextField()
    preparationmethod=models.TextField()
    preparationtime=models.IntegerField()
    fotos= models.ImageField(upload_to='receitasfotos/', blank=True, null=True)

    like = models.IntegerField(default=0)
    deslike = models.IntegerField(default=0)

   
   

    def __str__(self):
        return self.name