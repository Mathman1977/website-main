from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import OpgavenReeks,Opgave,Excercice
from django.utils import timezone
import time

class HomeView(ListView):
    model = OpgavenReeks
    template_name = 'level/home.html'
    fields = '__all__'
    # cats = Category.objects.all()
    # ordering = ['-post_date']
    ordering = ['-id']


# class OpgavenReeksDetailView(DetailView):
#     model = OpgavenReeks
#     template_name = 'level/opgavenreeks_training.html'

#     def get_context_data(self, *args, **kwargs):
#         opgavenreeks = get_object_or_404(OpgavenReeks,id=self.kwargs['pk'])
#         context = super(OpgavenReeksDetailView, self).get_context_data(*args, **kwargs)
#         opgaven = Opgave.objects.all()
#         opgaven = opgaven.filter(opgavenreeks=opgavenreeks.id)
#         index = 0
#         opgave = opgaven.first()
#         context["opgave"] = opgave
#         return context



def training(request,pk):
    datum_gemaakt = timezone.now()
    opgavenreeks = get_object_or_404(OpgavenReeks,id=pk)
    opgavenreeks_id = opgavenreeks.id
    opgaven = Opgave.objects.all()
    opgaven = opgaven.filter(opgavenreeks=opgavenreeks.id)
    aantal = opgaven.count()
    opgave = opgaven.first()
    opgave_id = opgave.id
    opgave_1 = opgave.id #eerste opgave
    oefnr = opgave_id-opgave_1 + 1
    start = round(time.time(),)
    afgewerkt = (oefnr-1)/aantal*100
    jouw_tijd = 0
    context ={'opgavenreeks':opgavenreeks ,'opgave': opgave,
                'afgewerkt':afgewerkt,'oefnr':oefnr,
                'aantal':aantal,'jouw_tijd':jouw_tijd,
                'opgave_id': opgave_id,'start':start}
    if request.method == "POST":
        jouw_antwoord = request.POST['jouw_antwoord']
        vorige_start = int(request.POST['start'])
        opgave_id = int(request.POST['opgave_id'])
        jouw_tijd = int(request.POST['jouw_tijd'])

        opgave = opgaven.get(pk=opgave_id)
        if jouw_antwoord == "":
            foutmelding = "hey, je moet wel iets invullen hé!"
            start = vorige_start
            opgave = opgaven.get(pk=opgave_id)
            oefnr = opgave_id-opgave_1 + 1

            afgewerkt = (oefnr-1)/aantal*100
            context ={'foutmelding':foutmelding,'opgavenreeks':opgavenreeks ,
                        'opgavenreeks_id':opgavenreeks_id,
                        'afgewerkt':afgewerkt,'oefnr':oefnr,'aantal':aantal,
                        'jouw_tijd':jouw_tijd,
                        'opgave': opgave, 'opgave_id':opgave_id,
                        'start':start }
            return render(request, 'level/opgavenreeks_training.html', context)
        # oefeningen = Excercice.objects.all()
        # oefening_exists = oefeningen.filter(player = request.user,opgave=opgave,oef_datum = datum_gemaakt).count()
        # if oefening_exists != 0:
        #     foutmelding = "sorry, je hebt deze vandaag al gemaakt!"
        #     start = vorige_start
        #     gemaakte_oefeningen = oefeningen.filter(player=request.user,oef_datum=datum_gemaakt)
        #     opgave_id = gemaakte_oefeningen.last().id
        #     opgave_id += 1
        #     if (opgave_id - aantal + 1) < opgave_1:
        #         opgave = opgaven.get(pk=opgave_id)
        #         context ={'foutmelding':foutmelding, 'opgavenreeks':opgavenreeks,
        #                 'afgewerkt':afgewerkt,'oefnr':oefnr,'aantal':aantal,
        #                 'opgave': opgave, 'opgave_id': opgave_id,'start':start}
        #         return render(request, 'level/opgavenreeks_training.html', context)

        #     else:
        #         return render(request, 'level/opgavenreeks_resultaten.html', context)

        start = round(time.time(), )
        delta = start - vorige_start
        check = False
        fast_check = False
        if jouw_antwoord == opgave.opl:
            check = True
        if delta < opgave.strtijd:
            fast_check = True
        oef = Excercice(player= request.user,opgave=opgave,jouw_antwoord=jouw_antwoord,juist_fout=check,
            jouw_delta=delta, snelheid=fast_check, oef_datum=datum_gemaakt)
        oef.save()
        if (opgave_id - aantal + 1) < opgave_1:
            opgave_id += 1
            oefnr = opgave_id-opgave_1 + 1
            afgewerkt = round((oefnr-1)/aantal*100)
            opgave = opgaven.get(pk=opgave_id)
            context = {'opgavenreeks':opgavenreeks ,'opgaven':opgaven ,
                          'opgavenreeks_id':opgavenreeks_id,
                        'afgewerkt':afgewerkt,'oefnr':oefnr,'aantal':aantal,
                        'jouw_tijd':jouw_tijd,
                        'opgave': opgave, 'opgave_id':opgave_id,
                        'start':start}
            return render(request, 'level/opgavenreeks_training.html', context)

        else:
            context = {'opgavenreeks':opgavenreeks, 'afgewerkt':100}
            return render(request, 'level/naarresultaten.html', context)


    return render(request, 'level/opgavenreeks_training.html', context)


def resultaten(request,opgavenreeks_id):
        datum_gemaakt = timezone.now()
        opgavenreeks = get_object_or_404(OpgavenReeks,id=opgavenreeks_id)
        opgaven = Opgave.objects.all()
        opgaven = opgaven.filter(opgavenreeks=opgavenreeks.id)
        aantal = opgaven.count()
        opgave = opgaven.first()
        opgave_id = opgave.id
        opgave_1 = opgave.id #eerste opgave
        fouten = []
        slowmos = []
        uitwerkingen = []
        oefeningen = Excercice.objects.all()
        oefeningen = oefeningen.filter(player = request.user,oef_datum = datum_gemaakt)
        delta = 0
        streeftijd = 0
        for oef in oefeningen:
            if oef.juist_fout == False:
                fouten.append(oef.opgave.id - opgave_1 + 1)
            if oef.snelheid == False:
                slowmos.append(oef.opgave.id - opgave_1 + 1)
            uitwerkingen.append(oef.opgave.id - opgave_1 + 1)
            delta += oef.jouw_delta
            opgave_id = oef.opgave.id
            streeftijd += opgaven.get(id=opgave_id).strtijd

        aantal_fouten = len(set(fouten))
        aantal_juist = aantal - aantal_fouten
        aantal_slowmo = len(set(slowmos))
        aantal_snel = aantal - aantal_slowmo

        delta_minuten = delta//60
        delta_seconden = delta%60
        streeftijd_minuten= streeftijd//60
        streeftijd_seconden = streeftijd%60


        context = {'title': 'Resultaten',
                    'opgavenreeks':opgavenreeks ,
                    'fouten':fouten,
                    'slowmos':slowmos,
                    'uitwerkingen':uitwerkingen,
                    'aantal':aantal,
                    'aantal_juist':aantal_juist,
                    'delta_minuten':delta_minuten,
                    'delta_seconden':delta_seconden,
                    'streeftijd_minuten':streeftijd_minuten,
                    'streeftijd_seconden':streeftijd_seconden,
                    'delta':delta,
                    'streeftijd':streeftijd,
                    }
        return render(request, 'level/opgavenreeks_resultaten.html', context)




def uitgewerkt(request, opgavenreeks_id, uitw):
    opgavenreeks = get_object_or_404(OpgavenReeks, pk=opgavenreeks_id)
    opgaven = opgavenreeks.opgave_set.all()
    opgave = opgaven.first()
    opgave_1 = opgave.id #eerste opgave
    opgave_id = opgave_1 + uitw - 1
    opgave = opgaven.get(pk=opgave_id)
    datum_gemaakt = timezone.now()
    oefeningen = Excercice.objects.all()
    oefeningen = oefeningen.filter(player = request.user,oef_datum = datum_gemaakt)
    uitwerkingen = []
    oefnr = opgave_id-opgave_1 + 1
    for oef in oefeningen:
        uitwerkingen.append(oef.opgave.id - opgave_1 + 1)

    if oefeningen.filter(player = request.user,oef_datum = datum_gemaakt,opgave=opgave).exists() ==  False:
        foutmelding = "Hei maatje, niet zeuren hé, zou je niet eerst es zelf proberen?"
    else:
        foutmelding = ''
    titel = f'Uitgewerkte oefening {uitw}'
    context = {'title': 'titel',
                        'opgavenreeks':opgavenreeks ,
                        'opgaven':opgaven,
                        'opgave':opgave,
                        'uitw':uitw,
                        'foutmelding':foutmelding,
                         'uitwerkingen':uitwerkingen,
                         'oefnr':oefnr

                        }


    return render(request, 'level/uitgewerkt.html', context)
