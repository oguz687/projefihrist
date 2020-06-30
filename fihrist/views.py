from random import randint

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.views.generic import ListView, TemplateView
from numpy.random.mtrand import random

from fihrist.models import Personel, Amirlik, Mudurluk, AmirlikYetki, MudurlukYetki


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


def amirlik(args):
    amirlik = Amirlik.objects.get_or_create(amirlik="Soyisimler")
    return amirlik



def mudurluk(args):
    mudurluk = Mudurluk.objects.get_or_create(mudurluk="Sehir")
    return mudurluk


def amirlikyetki(args):
    amirlikyetki=AmirlikYetki.objects.get_or_create(amirlik_yetki=False)
    return amirlikyetki


def mudurlukyetki(args):
    mudurlukyetki = MudurlukYetki.objects.get_or_create(mudurluk_yetki=False)
    return mudurlukyetki


def ekle(request):
    from pathlib import Path
    import pandas as pd

    from fihrist.models import Personel

    pathd = Path("C:\\Users\\oguzhan.ozturk\\Desktop\\xx\\calisan_data.csv")
    data = pd.read_csv(pathd)
    data2 = pd.DataFrame(data,
                         columns=['Isimler', 'Soyisimler', 'TelefonTuru', 'Departman', 'Sehir', 'DogumTarihi', 'Maas',
                                  'Telefon', 'mail'])



    objs = [
        Personel(
            # amirlik=Amirlik(amirlik=amirlik), mudurluk=Mudurluk(mudurluk=mudurluk),
            isim=row["Isimler"], sicil=randint(1, 100000000),
            telefon=randint(1, 100000000),
            tc=row["Telefon"], adres=row["Departman"],
            # amirlik_yetki=AmirlikYetki(amirlik_yetki=amirlikyetki),
            # mudurluk_yetki_id=1,amirlik_yetki_id=2,yetki_id=3,mudurluk_yetki=MudurlukYetki(mudurluk_yetki=mudurlukyetki)
        )
        for index, row in data2.head(n=data2.size).iterrows()
    ]
    msg = Personel.objects.bulk_create(objs=objs)


    return HttpResponse(print("rew"))
