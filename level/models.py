from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import datetime,date
from PIL import Image
from django.contrib.auth.models import User



class OpgavenReeks(models.Model):
    titel = models.CharField(max_length=100)
    foto= models.ImageField(upload_to='reeksfotos/',null=True,blank=True)#default = costume hoedje af
    uitleg = models.TextField()
    datum = models.DateField(auto_now_add=True)
    soort =  models.CharField(max_length=100)
    onderwerp =  models.CharField(max_length=100)
    DIFFICULTIES = (
        ('*', 'Easy'),
        ('**', 'Doable'),
        ('***', 'Hard'),
        ('****', 'Die hard'),
    )
    glob_moeilkhgr = models.CharField(max_length=4, choices=DIFFICULTIES)
    glob_strtijd = models.IntegerField() #later vervangen door som van opgaven of door gem doorlooptijd studenten
    vereiste_level = models.CharField(default='Level 4',max_length=50)
    nodig_materiaal = models.CharField(max_length=200)
    joke = models.ImageField(upload_to='reeksfotos/',null=True,blank=True)#default = costume hoedje af
    website_url = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = ('OpgavenReeks')
        verbose_name_plural =('OpgavenReeksen')
        # ordering = ('datum')

    def __str__(self):
        return self.titel

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)) )
        return reverse('home')



class Opgave(models.Model):
    opgavenreeks = models.ForeignKey(OpgavenReeks, on_delete=models.CASCADE)
    onderwerp =  models.CharField(max_length=100)
    opg_titel = models.CharField(max_length=100,blank=True)
    opg_foto = models.ImageField(blank=True, null=True)
    opl_foto = models.ImageField(blank=True, null=True)
    opl = models.CharField(max_length=100)
    type_antw = models.CharField(max_length=50,default='input_antw')
    DIFFICULTIES = (
        ('*', 'Easy'),
        ('**', 'Doable'),
        ('***', 'Hard'),
        ('****', 'Die hard'),
    )
    moeilkhgr = models.CharField(max_length=4, choices=DIFFICULTIES)
    strtijd = models.IntegerField()

    class Meta:
        verbose_name = ('Opgave')
        verbose_name_plural =('Opgaven')
        # ordering = ('datum')

    def __str__(self):
        return '%s - Opgave %i' % (self.opgavenreeks.titel, self.id)

    # def get_absolute_url(self):
    #     return reverse ('opg-detail', kwargs={'pk':self.pk})



class Excercice(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    opgave = models.ForeignKey(Opgave, on_delete=models.CASCADE)
    jouw_antwoord = models.CharField(max_length=100)
    jouw_delta = models.IntegerField()
    oef_datum = models.DateField(auto_now_add=True) #models.DateTimeField('datum_gemaakt')
    juist_fout = models.BooleanField(default=False)
    snelheid = models.BooleanField(default=False)
    def controleer(self):
        if self.jouw_antwoord == self.opgave.opl:
            juist_fout = True
        else:
            juist_fout = False


    def __str__(self):
        return '%s - %s' % (self.player,self.opgave)

    class Meta:
        verbose_name = ('Oefening')
        verbose_name_plural =('Oefeningen')
        # ordering = ('datum')

    def get_absolute_url(self):
        return reverse('home')

