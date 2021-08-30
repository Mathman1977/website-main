from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from datetime import datetime,date
from django.urls import reverse
from PIL import Image

class Reeks(models.Model):
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
    vereiste_level = models.CharField(default='MB1',max_length=50)
    nodig_materiaal = models.CharField(max_length=200)
    joke = models.ImageField(upload_to='reeksfotos/',null=True,blank=True)#default = costume hoedje af
    website_url = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = ('Reeks')
        verbose_name_plural =('Reeksen')
        # ordering = ('datum')

    def __str__(self):
        return self.titel

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)) )
        return reverse('home')




class Opgave(models.Model):
    reeks = models.ForeignKey(Reeks, on_delete=models.CASCADE)
    onderwerp =  models.CharField(max_length=100)
    opg_titel = models.CharField(max_length=100,blank=True)
    # opg_foto = models.ImageField(blank=True, null=True)
    # opl_foto = models.ImageField(blank=True, null=True)
    opl = models.IntegerField()
    moeilkhgr = models.IntegerField()
    # moeilkhgr = models.TextChoices('stars', '* ** ***')
    strtijd = models.IntegerField()

    class Meta:
        verbose_name = ('Opgave')
        verbose_name_plural =('Opgaven')
        # ordering = ('datum')

    def __str__(self):
        return 'Opgave' + str(self.id)

    # def get_absolute_url(self):
    #     return reverse ('opg-detail', kwargs={'pk':self.pk})

class Oefening(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    opgave = models.ForeignKey(Opgave, on_delete=models.CASCADE)
    antwoord = models.IntegerField(blank=True)
    delta = models.IntegerField()
    oef_datum = models.DateTimeField('datum_gemaakt')

    # def __str__(self):
    #     return self.student + self.opgave.id

    class Meta:
        verbose_name = ('Oefening')
        verbose_name_plural =('Oefeningen')
        # ordering = ('datum')

