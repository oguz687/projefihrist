from random import randint

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.views.generic import ListView, TemplateView
from numpy.random.mtrand import random

from fihrist.models import Personel, Amirlik, Mudurluk


# def get_queryset(self):  # new
#     template = loader.get_template('fihrist/base.html')
#     return self.model.objects.filter(isim__icontains="Deneme")
#
def page(request):
    template = loader.get_template('fihrist/base.html')
    personel = Personel.objects.all()
    context = {
        'personel': personel,
    }
    # print("yetki 0")
    return HttpResponse(template.render(context, request))


def sec(request):
    template = loader.get_template('fihrist/base.html')
    query = request.GET.get('qq')

    personeltek = Personel.objects.get(sicil__exact=query)
    context = {
        'personeltek': personeltek,
    }

    return HttpResponse(template.render(context, request))


def results(request):
    template = loader.get_template('fihrist/base.html')
    # personel = Personel.objects.all()
    query = request.GET.get('q')
    personel = Personel.objects.filter(Q(isim__icontains=query) | Q(tc__icontains=query) | Q(sicil__icontains=query))
    # if request.method == 'GET':
    #     query = request.GET.get('q')
    #     if query:
    #         context = Personel.objects.filter(Q(isim__icontains=query) | Q(tc__icontains=query))
    #         return HttpResponse(template.render(context,request))
    context = {
        'personel': personel,
    }
    # print("yetki 0")
    return HttpResponse(template.render(context, request))


def ekle(request):
    from pathlib import Path
    import pandas as pd

    from fihrist.models import Personel

    pathd = Path("C:\\Users\\atessu\\Desktop\\xx\\calisan_data.csv")
    data = pd.read_csv(pathd)
    data2 = pd.DataFrame(data,
                         columns=['Isimler', 'Soyisimler', 'TelefonTuru', 'Departman', 'Sehir', 'DogumTarihi', 'Maas',
                                  'Telefon', 'mail'])
    personel = Personel.objects.get_or_create(isim=data2["Isimler"], sicil=randint(1, 10000),
                                              telefon=randint(1, 1000000),
                                              amirlik=Amirlik(amirlik=data2["Soyisimler"]),
                                              mudurluk=Mudurluk(mudurluk=data2["Departman"])
                                              , tc=data2["Telefon"], adres=data2["Departman"])
