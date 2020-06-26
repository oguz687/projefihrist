from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.views.generic import ListView, TemplateView

from fihrist.models import Personel


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


def results(request):
    template = loader.get_template('fihrist/base.html')
    # personel = Personel.objects.all()
    query = request.GET.get('q')
    personel = Personel.objects.filter(Q(isim__icontains=query) | Q(tc__icontains=query)|Q(sicil__icontains=query))
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
