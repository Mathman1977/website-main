from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from .models import Reeks, Opgave,Oefening
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import datetime
from datetime import datetime
import time
from PIL import Image

class HomeView(ListView):
    model = Reeks
    template_name = 'mb4/home.html'
    # cats = Category.objects.all()
    # ordering = ['-post_date']
    ordering = ['-id']

    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(HomeView, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context

def index(request):
    laatste_oef_lijst = Reeks.objects.order_by('-datum')[:5]
    context = {'laatste_oef_lijst': laatste_oef_lijst,'title':'overzicht'}
    return render(request, 'mb4/index.html', context)


# moet nog een detailpagina over de oefening komen
def detail(request, reeks_id):
    reeks = get_object_or_404(Reeks, pk=reeks_id)
    opgave_id = 1
    context = {'title': reeks.titel, 'reeks': reeks,
                'reeks_id': reeks_id, 'opgave_id':opgave_id}
    return render(request, 'mb4/detail.html', context)

def training(request, reeks_id, opgave_id):
    datum_gemaakt = datetime.now()
    reeks = get_object_or_404(Reeks, pk=reeks_id)
    opgaven = reeks.opgave_set.all()
    opgave_id = opgave_id
    opgave = opgaven.get(pk=opgave_id)
    aantal = opgaven.count()
    opgave = opgaven.first()
    start = round(time.time(), )
    context = {'title': 'Training','reeks': reeks,
             'opgave': opgave, 'start':start,
             'reeks_id': reeks_id, 'opgave_id':opgave_id
                }
    if request.method == "POST":

        jouw_antwoord = request.POST['jouw_antwoord']
        vorige_start = int(request.POST['start'])
        opgave_id = int(request.POST['opgave_id'])
        if jouw_antwoord == "":
            foutmelding = "hey, je moet wel iets kiezen hé!"
            color = 'warning'
            start = vorige_start
            opgave = opgaven.get(pk=opgave_id)
            context = {'title': 'Helaba','reeks': reeks,
                        'opgave': opgave, 'start':start,
                        'foutmelding': foutmelding,
                        'reeks_id': reeks_id, 'opgave_id':opgave_id
            }
            return render(request, 'mb4/training.html', context)
        jouw_antwoord = int(request.POST['jouw_antwoord'])
        start = round(time.time(), )
        delta = start - vorige_start
        oef = Oefening(student= request.user,opgave=opgave,antwoord=jouw_antwoord,delta=delta,oef_datum=datum_gemaakt)
        oef.save()
        if opgave_id < aantal:
            opgave_id += 1
            opgave = opgaven.get(pk=opgave_id)
            context = {'title': 'Training','reeks': reeks,
                        'opgave': opgave, 'start':start,
                        'reeks_id': reeks_id, 'opgave_id':opgave_id
                        }
            return render(request, 'mb4/training.html', context)
        else:
            return render(request, 'mb4/naarresultaten.html', context)

    return render(request, 'mb4/training.html', context)

def resultaten(request,reeks_id):
    reeks = get_object_or_404(Reeks, pk=reeks_id)
    reeks_opgaven = reeks.opgave_set.all()
    aantal = reeks_opgaven.count()
    reeks_oefeningen = Oefening.objects.filter(student=request.user)
    juiste_opl = [opg.opl for opg in reeks_opgaven]
    delta_opl = [opg.strtijd for opg in reeks_opgaven]
    antwoorden = [oef.antwoord for oef in reeks_oefeningen]
    delta_antwoorden = [oef.delta for oef in reeks_oefeningen]
    foute_antwoorden = []
    slowmo_antwoorden = []
    for i in range(len(juiste_opl)):
        if juiste_opl[i]!=antwoorden[i]:
            foute_antwoorden.append(i+1)
    for i in range(len(juiste_opl)):
        if delta_opl[i] < delta_antwoorden[i]:
            slowmo_antwoorden.append(i+1)
    aantal_fouten = len(set(foute_antwoorden))
    aantal_juist = aantal - aantal_fouten

    print(juiste_opl)
    print(antwoorden)
    print(foute_antwoorden)
    print(slowmo_antwoorden)

    context = {'title': 'Resultaten','reeks': reeks,
                        'reeks_id': reeks_id,
                        'reeks_opgaven': reeks_opgaven,
                        'foute_antwoorden':foute_antwoorden,
                        'slowmo_antwoorden':slowmo_antwoorden,
                        'reeks_oefeningen':reeks_oefeningen,
                        'aantal':aantal,
                        'aantal_juist':aantal_juist
            }

    return render(request, 'mb4/resultaten.html',context)


def uitgewerkt(request, reeks_id, opgave_id):
    reeks = get_object_or_404(Reeks, pk=reeks_id)
    opgaven = reeks.opgave_set.all()
    opgave_id = opgave_id
    opgave = opgaven.get(pk=opgave_id)

    title= 'uitgewerkte oefening'
    return render(request, 'mb4/uitgewerkt.html', {
        'title': title, 'opgave': opgave ,
        'reeks_id':reeks_id})
