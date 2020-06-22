from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.views.generic import ListView

from fihrist.models import Personel

class PersonelView(ListView):
    model = Personel
    template = loader.get_template('fihrist/index.html')

    def get_queryset(self):  # new
        return Personel.objects.filter(isim__icontains='Deneme')


    def results(request,personel):
        template = loader.get_template('fihrist/index.html')
        # personel = Personel.objects.all()
        personel=self.get_queryset()
        context = {
            'personel': personel,
        }
        print("yetki 0")
        return HttpResponse(template.render(context, request))

