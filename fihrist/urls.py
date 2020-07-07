from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from wkhtmltopdf.views import PDFTemplateView

from . import views

urlpatterns = [
                  # post views
                  path('', views.page, name='page'),
                  path('personeller/', views.hepsi, name='hepsi'),
                  path('ara/', views.results, name='results'),
                  path('ara/sec/', views.sec, name='sec'),
                  path('ekle/', views.ekle, name='ekle'),
                  path('askerlikdilekce/', views.askerlikdilekce, name='askerlikdilekce'),
                  path('askerlikustyazi/', views.askerlikustyazi, name='askerlikustyazi'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
