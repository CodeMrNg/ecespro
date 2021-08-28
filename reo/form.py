from django import forms

class SerieForm(forms.Form):
    F = (
        (1, 'Faible'),
        (2, 'Moyen'),
        (3, 'Bon'),
    )
    choice = forms.ChoiceField(label='Maths', widget=forms.RadioSelect, choices=F)
    choice2 = forms.ChoiceField(label='Physique', widget=forms.RadioSelect, choices=F)
    choice3 = forms.ChoiceField(label='Histoire/Geo', widget=forms.RadioSelect, choices=F)
    choice4 = forms.ChoiceField(label='S.V.T', widget=forms.RadioSelect, choices=F)



class Aform(forms.Form):
    F = (
        (1, 'Faible'),
        (2, 'Moyen'),
        (3, 'Bon'),
    )
    choice = forms.ChoiceField(label='Maths', widget=forms.RadioSelect, choices=F)
    choice2 = forms.ChoiceField(label='philosopie', widget=forms.RadioSelect, choices=F)
    choice3 = forms.ChoiceField(label='Histoire/Geo', widget=forms.RadioSelect, choices=F)
    choice4 = forms.ChoiceField(label='Francais', widget=forms.RadioSelect, choices=F)

class Eform(forms.Form):
    F = (
        (1, 'Faible'),
        (2, 'Moyen'),
        (3, 'Bon'),
    )
    choice = forms.ChoiceField(label='Maths', widget=forms.RadioSelect, choices=F)
    choice2 = forms.ChoiceField(label='Dessin', widget=forms.RadioSelect, choices=F)
    choice3 = forms.ChoiceField(label='Phisique chime', widget=forms.RadioSelect, choices=F)
    choice4 = forms.ChoiceField(label='Francais', widget=forms.RadioSelect, choices=F)






class Rform(forms.Form):
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
    nom = forms.CharField()
    serie = forms.ChoiceField(label='Entrez votre serie', choices=S)
    nbfois = forms.ChoiceField(label='Combien de  fois avez vous manquez votre examen', choices=N)
    age = forms.IntegerField()
    score = forms.HiddenInput()