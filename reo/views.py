from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from reo.models import Recup, Recupform
from reo.form import SerieForm, Aform, Rform, Eform

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = Rform(request.POST)
        if form.is_valid():
            serie = form.cleaned_data['serie']
            if serie == 'A':
                return HttpResponseRedirect(reverse('serieA') )
            elif serie == 'D':
                return HttpResponseRedirect(reverse('serieD') )
            elif serie == "E":
                return HttpResponseRedirect(reverse('serieE') )
            else:
                return HttpResponseRedirect(reverse('serie') )   
    else:
        form = Rform()
    template = 'index.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def serie(request):
    if request.method == 'POST':
        form = SerieForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data['choice']
            choice2 = form.cleaned_data['choice2']
            choice3 = form.cleaned_data['choice3']
            choice4 = form.cleaned_data['choice4']
            somme = int(choice) + int(choice2) + int(choice3) + int(choice4)
            m = 'serie.html'
            if somme > 9:
                text = 'C, BG, D'
                return render (request, m , {'text':text, 'form':form})
            elif somme >=6:
                text = 'BG, D'
                return render (request, m , {'text':text, 'form':form})
            elif somme <=5:
                text = 'BG' 
                return render (request, m , {'text':text, 'form':form})
    else:
        form = SerieForm()
    context = {
        'form': form,
    }
    template = 'serie.html'
    return render(request, template, context)



def serieA(request):
    if request.method == 'POST':
        form = Aform(request.POST)
        if form.is_valid():
            choice = form.cleaned_data['choice']
            choice2 = form.cleaned_data['choice2']
            choice3 = form.cleaned_data['choice3']
            choice4 = form.cleaned_data['choice4']
            somme = int(choice) + int(choice2) + int(choice3) + int(choice4)
            m = 'serieA.html'
            if somme > 9:
                text = 'A, G1'
                return render (request, m , {'text':text, 'form':form})
            elif somme >=6:
                text = 'G1, A'
                return render (request, m , {'text':text, 'form':form})
            elif somme <=5:
                text = 'G1' 
                return render (request, m , {'text':text, 'form':form})
    else:
        form = Aform()
    context = {
        'form': form,
    }
    template = 'serieA.html'
    return render(request, template, context)

def serieD(request):
    if request.method == 'POST':
        form = SerieForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data['choice']
            choice2 = form.cleaned_data['choice2']
            choice3 = form.cleaned_data['choice3']
            choice4 = form.cleaned_data['choice4']
            somme = int(choice) + int(choice2) + int(choice3) + int(choice4)
            m = 'serieD.html'
            if somme > 9:
                text = 'BG, D'
                return render (request, m , {'text':text, 'form':form})
            elif somme >=6:
                text = 'BG'
                return render (request, m , {'text':text, 'form':form})
            elif somme <=5:
                text = 'BG' 
                return render (request, m , {'text':text, 'form':form})
    else:
        form = SerieForm()
    context = {
        'form': form,
    }
    template = 'serie.html'
    return render(request, template, context)


def serieE(request):
    if request.method == 'POST':
        form = Eform(request.POST)
        if form.is_valid():
            choice = form.cleaned_data['choice']
            choice2 = form.cleaned_data['choice2']
            choice3 = form.cleaned_data['choice3']
            choice4 = form.cleaned_data['choice4']
            somme = int(choice) + int(choice2) + int(choice3) + int(choice4)
            m = 'serieE.html'
            if somme > 9:
                text = 'C, BG, D'
                return render (request, m , {'text':text, 'form':form})
            elif somme >=6:
                text = 'BG, D'
                return render (request, m , {'text':text, 'form':form})
            elif somme <=5:
                text = 'BG' 
                return render (request, m , {'text':text, 'form':form})
    else:
        form = Eform()
    context = {
        'form': form,
    }
    template = 'serieE.html'
    return render(request, template, context)





























def result(request):
    pass