# -*- coding: utf-8 -*-

import io
from random import randint
from django.utils.encoding import uri_to_iri
from django.utils.encoding import iri_to_uri
from django.db.models import Q
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader, RequestContext
from django.utils.encoding import smart_str
from django.views.generic import ListView, TemplateView
from django.views.generic.base import View
from numpy.random.mtrand import random
from reportlab.pdfgen import canvas

from fihrist.models import Personel, Amirlik, Mudurluk, AmirlikYetki, MudurlukYetki
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from weasyprint import HTML
import tempfile


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
    form = request.GET.get('formsecc')
    context = {
        'personeltek': personeltek,
    }

    return HttpResponse(template.render(context, request))


def results(request):
    template = loader.get_template('fihrist/base.html')
    # personel = Personel.objects.all()
    query = request.GET.get('q')
    print(query)
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
    amirlikyetki = AmirlikYetki.objects.get_or_create(amirlik_yetki=False)
    return amirlikyetki


def mudurlukyetki(args):
    mudurlukyetki = MudurlukYetki.objects.get_or_create(mudurluk_yetki=False)
    return mudurlukyetki


def ekle(request):
    from pathlib import Path
    import pandas as pd

    from fihrist.models import Personel

    pathd = Path("C:\\Users\\oguzhan.ozturk\\Desktop\\xx\\calisan_data.csv")
    patht = Path("C:\\Users\\atessu\\Desktop\\xx\\calisan_data.csv")

    if patht.is_file():
        data = pd.read_csv(patht)
    else:
        data=pd.read_csv(pathd)

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


def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


# from io import BytesIO
# from django.http import HttpResponse
# from django.template.loader import get_template
#
# from xhtml2pdf import pisa
#
#
# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return None
#
#
# def pdf(request):
#     template = get_template('fihrist/deneme.html')
#     context = {
#         'pagesize': 'A4',
#
#     }
#     html = template.render(context)
#     pdf = render_to_pdf('fihrist/pdf/deneme.html', context)
#     if pdf:
#         response = HttpResponse(pdf, content_type='application/pdf')
#         filename = "Invoice_%s.pdf" % "12341231"
#         content = "inline; filename='%s'" % filename
#         download = request.GET.get("download")
#         if download:
#             content = "attachment; filename='%s'" % filename
#         response['Content-Disposition'] = content
#         return response
#     return HttpResponse("Not found")


def pdf(request):

    """Generate pdf."""
    # Model data
    # people = Personel.objects.all().order_by('mail')

    # Rendered
    # html_string = render_to_string('fihrist/pdf/deneme.html', {'people': "fdgfg"})
    # html = HTML(string=html_string)
    # result = html.write_pdf()
    #
    # # Creating http response
    # response = HttpResponse(content_type='application/pdf;')
    # response['Content-Disposition'] = 'inline; filename=list_people.pdf'
    # response['Content-Transfer-Encoding'] = 'binary'
    # with tempfile.NamedTemporaryFile(delete=True) as output:
    #     output.write(result)
    #     output.flush()
    #     with open(output.name, 'r') as x:
    #         response.write(output.read())
    #         return response
    # template = loader.get_template('fihrist/base.html')
    # personel = Personel.objects.all()
    # context = {
    #     'personel': personel,
    # }
    # # print("yetki 0")
    # return HttpResponse(template.render(context, request))

    # html_template = get_template('fihrist/pdf/deneme5.html')
    template = loader.get_template('fihrist/base.html')

    query = request.GET.get('qt')
    personel = Personel.objects.get(sicil__exact=query)
    context = {
        'personel': personel,
    }
    html_template2 = render_to_string('fihrist/pdf/deneme5.html',context,request=request)
    # html_template = render_to_string('fihrist/pdf/deneme5.html',{'personel' : personel.foto})
    pdf_file = HTML(string=html_template2).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="home_page.pdf"'
    return response
