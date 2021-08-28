from django.db import models
from django.forms import ModelForm


#creation du models

class Recup(models.Model):
    S = (
        ('A', 'A'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    )
    N = (
        (2 ,2),
        (3, 3),
        (3, 4),
    )
    name = models.CharField('Entrez votre nom SVP', max_length=50)
    serie = models.CharField('entrez serie', max_length=50, choices=S)
    nbfois = models.IntegerField('Combien de fois avez vous manquez votre examen ?',choices=N)
    age = models.IntegerField('Entrez votre age ')
    score = models.IntegerField()





class Recupform(ModelForm):
    class Meta:
        model = Recup
        fields = ['name', 'serie', 'nbfois', 'age']

    
